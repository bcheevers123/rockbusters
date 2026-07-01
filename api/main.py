"""Rockbusters FastAPI application entry point."""

import datetime
import sqlite3

import pytz
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

from api.config import Config
from api.content_bank import load_bank
from api.db import (
    get_leaderboard,
    get_user_score_today,
    has_correct_guess,
    has_revealed,
    init_db,
    record_guess,
    record_reveal,
    upsert_user,
)
from api.game_service import get_todays_set

# ---------------------------------------------------------------------------
# App startup
# ---------------------------------------------------------------------------

config = Config()
init_db(config.sqlite_path)
bank = load_bank(config.bank_path)

app = FastAPI(title="Rockbusters API")

# CORS
if config.allowed_origins == "*":
    origins = ["*"]
else:
    origins = [o.strip() for o in config.allowed_origins.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_conn() -> sqlite3.Connection:
    """Open a new SQLite connection with Row factory enabled."""
    conn = sqlite3.connect(config.sqlite_path)
    conn.row_factory = sqlite3.Row
    return conn


def format_date_british(d: datetime.date) -> str:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    return f"{d.day} {months[d.month - 1]} {d.year}"


# ---------------------------------------------------------------------------
# Pydantic request models
# ---------------------------------------------------------------------------


class ScoreRequest(BaseModel):
    user_id: str
    display_name: str
    set_id: str
    clue_number: int


class RevealRequest(BaseModel):
    user_id: str
    display_name: str
    set_id: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/today")
def today():
    """Return today's set — clues only, no answers or aliases."""
    todays_set = get_todays_set(bank, config)

    tz = pytz.timezone(config.timezone)
    local_date = datetime.datetime.now(tz).date()

    return {
        "set_id": todays_set.id,
        "title": todays_set.title,
        "topic": todays_set.topic,
        "intro": todays_set.intro,
        "prize": todays_set.prize,
        "date": format_date_british(local_date),
        "clues": [
            {
                "number": c.number,
                "initials": c.initials,
                "clue": c.clue,
            }
            for c in todays_set.clues
        ],
    }


@app.get("/api/leaderboard")
def leaderboard():
    """Return top players plus today_points for each."""
    todays_set = get_todays_set(bank, config)
    set_id = todays_set.id

    conn = get_conn()
    try:
        rows = get_leaderboard(conn)
        result = []
        for rank, row in enumerate(rows, start=1):
            today_pts = get_user_score_today(conn, row["user_id"], set_id)
            result.append(
                {
                    "rank": rank,
                    "display_name": row["display_name"],
                    "total_points": row["total_points"],
                    "today_points": today_pts,
                }
            )
    finally:
        conn.close()

    return {"leaderboard": result, "set_id": set_id}


@app.post("/api/score")
def score(req: ScoreRequest):
    """Record a correct answer for a user.

    Returns 400 if the user has already revealed, 409 if the clue was already
    scored.
    """
    conn = get_conn()
    try:
        upsert_user(conn, req.user_id, req.display_name)

        if has_revealed(conn, req.user_id, req.set_id):
            raise HTTPException(status_code=400, detail="User has already revealed answers.")

        if has_correct_guess(conn, req.user_id, req.set_id, req.clue_number):
            raise HTTPException(status_code=409, detail="Clue already scored for this user.")

        record_guess(conn, req.user_id, req.set_id, req.clue_number, is_correct=True)
        points_today = get_user_score_today(conn, req.user_id, req.set_id)
    finally:
        conn.close()

    return {"ok": True, "points_today": points_today}


@app.post("/api/reveal")
def reveal(req: RevealRequest):
    """Record that a user revealed answers. Idempotent."""
    tz = pytz.timezone(config.timezone)
    reveal_date = datetime.datetime.now(tz).date().isoformat()

    conn = get_conn()
    try:
        upsert_user(conn, req.user_id, req.display_name)
        record_reveal(conn, req.user_id, req.set_id, reveal_date)
    finally:
        conn.close()

    return {"ok": True}


@app.get("/api/user-status")
def user_status(user_id: str = Query(...), set_id: str = Query(...)):
    """Return a user's status for a given set."""
    conn = get_conn()
    try:
        revealed = has_revealed(conn, user_id, set_id)

        rows = conn.execute(
            """
            SELECT clue_number FROM guesses
            WHERE user_id = ? AND set_id = ? AND is_correct = 1
            ORDER BY clue_number
            """,
            (user_id, set_id),
        ).fetchall()
        correct_clues = [row[0] for row in rows]

        points_today = get_user_score_today(conn, user_id, set_id)
    finally:
        conn.close()

    return {
        "revealed": revealed,
        "correct_clues": correct_clues,
        "points_today": points_today,
    }
