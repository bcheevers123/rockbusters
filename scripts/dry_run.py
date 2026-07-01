"""Rockbusters dry-run script — exercises the full daily rotation without writing to the database."""

import datetime
import sqlite3
import sys
from pathlib import Path

# Resolve paths relative to this script so the script works from any working directory
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from api.config import Config
from api.content_bank import load_bank
from api.db import init_db, record_guess, upsert_user, has_correct_guess, record_reveal, get_leaderboard
from api.game_service import get_todays_set

BANK_PATH = ROOT / "data" / "rockbusters.yaml"


def format_date_british(date: datetime.date) -> str:
    """Format a date in British format (e.g., '1 July 2026')."""
    # Use %d which pads with zero, then strip leading zero if present
    formatted = date.strftime("%d %B %Y")
    if formatted[0] == "0":
        formatted = formatted[1:]
    return formatted


def main():
    # Initialise in-memory SQLite database
    # Note: We need to initialize using a temp file path, then open it in memory
    # because init_db opens/closes its own connection
    import tempfile

    # Create a temporary in-memory database by initializing with a file, then using memory mode
    # Actually, the simplest way is to just use file mode with temp file then we have persistence
    # But the requirement is in-memory. Let's initialize the memory database directly.

    conn = sqlite3.connect(":memory:")
    # Manually initialize the in-memory database
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER PRIMARY KEY
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id      TEXT PRIMARY KEY,
            display_name TEXT,
            created_at   TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS guesses (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      TEXT    NOT NULL,
            set_id       TEXT    NOT NULL,
            clue_number  INTEGER NOT NULL,
            is_correct   INTEGER NOT NULL,
            guessed_at   TEXT    NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS daily_reveals (
            user_id     TEXT NOT NULL,
            set_id      TEXT NOT NULL,
            reveal_date TEXT NOT NULL,
            PRIMARY KEY (user_id, set_id)
        )
    """)

    cur.execute("INSERT OR IGNORE INTO schema_version (version) VALUES (1)")
    conn.commit()

    # Load the bank
    bank = load_bank(str(BANK_PATH))

    # Get today's set
    config = Config()
    today_set = get_todays_set(bank, config)

    # Print quiz information
    print(f"\n{'=' * 60}")
    print(f"ROCKBUSTERS DAILY QUIZ")
    print(f"{'=' * 60}\n")
    print(f"Title: {today_set.title}")
    print(f"Date: {format_date_british(datetime.date.today())}")
    print(f"Intro: {today_set.intro}\n")

    # Print clues with initials
    print("CLUES:")
    for clue in today_set.clues:
        print(f"{clue.number}. [{clue.initials}] {clue.clue}")

    print(f"\n{'-' * 60}\n")

    # Simulate a correct guess
    user_id = "dry-run-user"
    print(f"Simulating correct guess for clue 1...\n")

    # Record the user
    upsert_user(conn, user_id, "Dry Run Player")

    # Record a correct guess
    record_guess(conn, user_id, today_set.id, 1, True)

    # Verify the guess was recorded
    has_correct = has_correct_guess(conn, user_id, today_set.id, 1)
    print(f"Has correct guess for clue 1: {has_correct}")

    # Simulate a reveal
    today_str = datetime.date.today().isoformat()
    record_reveal(conn, user_id, today_set.id, today_str)
    print(f"Revealed answers for {user_id}.\n")

    # Print answers
    print(f"ANSWERS:")
    for clue in today_set.clues:
        print(f"{clue.number}. {clue.answer}: {clue.reasoning}")

    # Print leaderboard
    leaderboard = get_leaderboard(conn)
    print(f"\n{'-' * 60}")
    print(f"LEADERBOARD:")
    if leaderboard:
        for entry in leaderboard:
            print(f"  {entry['display_name']}: {entry['total_points']} points")
    else:
        print("  (empty)")

    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
