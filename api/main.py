"""Rockbusters FastAPI application entry point."""

import contextlib
import datetime
import hashlib
import logging
import sqlite3
import threading
from datetime import datetime as _dt, timezone

import pytz
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

from api.config import Config
from api.content_bank import load_bank
from api.db import (
    _create_schema,
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
from api import sheets as sheets_module

# ---------------------------------------------------------------------------
# App startup
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)

config = Config()

# Sheets mode: in-memory SQLite rebuilt from Google Sheets on startup
_sheets_client = None
_mem_conn = None
_mem_lock = threading.Lock()

if config.sheets_enabled():
    _mem_conn = sqlite3.connect(":memory:", check_same_thread=False)
    _mem_conn.row_factory = sqlite3.Row
    _create_schema(_mem_conn)

    try:
        _sheets_client = sheets_module.get_sheets_client(config.google_service_account_json)
        data = sheets_module.load_all(_sheets_client, config.google_sheets_id)
        sheets_module.replay_into_db(_mem_conn, data)
        logger.info("Sheets mode: replayed %d users, %d guesses, %d reveals.",
                    len(data["users"]), len(data["guesses"]), len(data["daily_reveals"]))
    except Exception as e:
        logger.error("Sheets startup failed (%s) — falling back to file SQLite.", e)
        if _mem_conn is not None:
            try:
                _mem_conn.close()
            except Exception:
                pass
        _mem_conn = None
        _sheets_client = None
        init_db(config.sqlite_path)
else:
    init_db(config.sqlite_path)

bank = load_bank(config.bank_path)

app = FastAPI(title="Rockbusters API")

# CORS
if config.allowed_origins == "*":
    origins = ["*"]
else:
    origins = [o.strip() for o in config.allowed_origins.split(",")]

allow_credentials = "*" not in origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_conn() -> sqlite3.Connection:
    """Return the active SQLite connection (in-memory if Sheets mode, file otherwise)."""
    if _mem_conn is not None:
        return _mem_conn
    conn = sqlite3.connect(config.sqlite_path)
    conn.row_factory = sqlite3.Row
    return conn


def _close_conn(conn: sqlite3.Connection) -> None:
    """Close conn only if it is not the shared in-memory connection."""
    if conn is not _mem_conn:
        conn.close()


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
        with _mem_lock if _mem_conn is not None else contextlib.nullcontext():
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
        _close_conn(conn)

    return {"leaderboard": result, "set_id": set_id}


@app.post("/api/score")
def score(req: ScoreRequest):
    """Record a correct answer for a user.

    Returns 400 if the user has already revealed, 409 if the clue was already
    scored.
    """
    conn = get_conn()
    try:
        _lock_ctx = _mem_lock if _mem_conn is not None else contextlib.nullcontext()
        with _lock_ctx:
            upsert_user(conn, req.user_id, req.display_name)

            if has_revealed(conn, req.user_id, req.set_id):
                raise HTTPException(status_code=400, detail="User has already revealed answers.")

            if has_correct_guess(conn, req.user_id, req.set_id, req.clue_number):
                raise HTTPException(status_code=409, detail="Clue already scored for this user.")

            record_guess(conn, req.user_id, req.set_id, req.clue_number, is_correct=True)

            points_today = get_user_score_today(conn, req.user_id, req.set_id)

        if _sheets_client:
            _now = _dt.now(timezone.utc).isoformat()
            sheets_module.sheets_write_with_retry(
                sheets_module.upsert_user_row,
                _sheets_client, config.google_sheets_id,
                req.user_id, req.display_name, _now,
            )
            sheets_module.sheets_write_with_retry(
                sheets_module.append_guess,
                _sheets_client, config.google_sheets_id,
                {
                    "user_id": req.user_id,
                    "set_id": req.set_id,
                    "clue_number": req.clue_number,
                    "is_correct": 1,
                    "guessed_at": _now,
                },
            )
    finally:
        _close_conn(conn)

    return {"ok": True, "points_today": points_today}


@app.post("/api/reveal")
def reveal(req: RevealRequest):
    """Record that a user revealed answers. Idempotent."""
    tz = pytz.timezone(config.timezone)
    reveal_date = datetime.datetime.now(tz).date().isoformat()

    conn = get_conn()
    try:
        _lock_ctx = _mem_lock if _mem_conn is not None else contextlib.nullcontext()
        with _lock_ctx:
            upsert_user(conn, req.user_id, req.display_name)
            record_reveal(conn, req.user_id, req.set_id, reveal_date)

        if _sheets_client:
            _now = _dt.now(timezone.utc).isoformat()
            sheets_module.sheets_write_with_retry(
                sheets_module.upsert_user_row,
                _sheets_client, config.google_sheets_id,
                req.user_id, req.display_name, _now,
            )
            sheets_module.sheets_write_with_retry(
                sheets_module.append_reveal,
                _sheets_client, config.google_sheets_id,
                {
                    "user_id": req.user_id,
                    "set_id": req.set_id,
                    "reveal_date": reveal_date,
                },
            )
    finally:
        _close_conn(conn)

    return {"ok": True}


@app.get("/api/user-status")
def user_status(user_id: str = Query(...), set_id: str = Query(...)):
    """Return a user's status for a given set."""
    conn = get_conn()
    try:
        with _mem_lock if _mem_conn is not None else contextlib.nullcontext():
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
        _close_conn(conn)

    return {
        "revealed": revealed,
        "correct_clues": correct_clues,
        "points_today": points_today,
    }


_DEV_PASSCODE_HASH = "7cad4eb0e04bd259d1291faa24c9b04a52cb6697ede50931cde44e046019c20d"


@app.post("/api/admin/reset-leaderboard")
def admin_reset_leaderboard(secret: str = Query(...)):
    """Clear all leaderboard data (guesses, reveals, users) from Sheets and in-memory DB."""
    secret_hash = hashlib.sha256(secret.strip().encode()).hexdigest()
    if secret_hash != _DEV_PASSCODE_HASH:
        raise HTTPException(status_code=403, detail="Forbidden")

    conn = get_conn()
    try:
        with _mem_lock if _mem_conn is not None else contextlib.nullcontext():
            conn.execute("DELETE FROM guesses")
            conn.execute("DELETE FROM daily_reveals")
            conn.execute("DELETE FROM users")
            conn.commit()
    finally:
        _close_conn(conn)

    if _sheets_client:
        sh = _sheets_client.open_by_key(config.google_sheets_id)
        for tab_name in ["guesses", "daily_reveals", "users"]:
            ws = sh.worksheet(tab_name)
            all_vals = ws.get_all_values()
            if len(all_vals) > 1:
                ws.delete_rows(2, len(all_vals))

    return {"ok": True, "message": "Leaderboard reset."}
