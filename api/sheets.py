"""Google Sheets persistence layer for Rockbusters."""

import json
import logging
import sqlite3
import time

import gspread

logger = logging.getLogger(__name__)

_SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]


def get_sheets_client(json_creds: str) -> gspread.Client:
    """Authenticate with a service account JSON string and return a gspread client."""
    creds_dict = json.loads(json_creds)
    return gspread.service_account_from_dict(creds_dict, scopes=_SCOPES)


def load_all(client: gspread.Client, sheet_id: str) -> dict:
    """Read all three tabs from the sheet. Returns dict with keys: users, guesses, daily_reveals."""
    sh = client.open_by_key(sheet_id)
    return {
        "users": sh.worksheet("users").get_all_records(),
        "guesses": sh.worksheet("guesses").get_all_records(),
        "daily_reveals": sh.worksheet("daily_reveals").get_all_records(),
    }


def replay_into_db(conn: sqlite3.Connection, data: dict) -> None:
    """Bulk-insert all rows from Sheets data into an already-initialised SQLite connection."""
    for row in data.get("users", []):
        conn.execute(
            "INSERT OR IGNORE INTO users (user_id, display_name, created_at) VALUES (?, ?, ?)",
            (row["user_id"], row["display_name"], row["created_at"]),
        )

    for row in data.get("guesses", []):
        conn.execute(
            """
            INSERT OR IGNORE INTO guesses (user_id, set_id, clue_number, is_correct, guessed_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                row["user_id"],
                row["set_id"],
                int(row["clue_number"]),
                int(row["is_correct"]),
                row["guessed_at"],
            ),
        )

    for row in data.get("daily_reveals", []):
        conn.execute(
            "INSERT OR IGNORE INTO daily_reveals (user_id, set_id, reveal_date) VALUES (?, ?, ?)",
            (row["user_id"], row["set_id"], row["reveal_date"]),
        )

    conn.commit()


def append_guess(client: gspread.Client, sheet_id: str, row: dict) -> None:
    """Append one guess row to the guesses tab."""
    sh = client.open_by_key(sheet_id)
    ws = sh.worksheet("guesses")
    ws.append_row([
        row["user_id"],
        row["set_id"],
        row["clue_number"],
        row["is_correct"],
        row["guessed_at"],
    ])


def append_reveal(client: gspread.Client, sheet_id: str, row: dict) -> None:
    """Append one reveal row to the daily_reveals tab."""
    sh = client.open_by_key(sheet_id)
    ws = sh.worksheet("daily_reveals")
    ws.append_row([row["user_id"], row["set_id"], row["reveal_date"]])


def upsert_user_row(
    client: gspread.Client,
    sheet_id: str,
    user_id: str,
    display_name: str,
    created_at: str,
) -> None:
    """Find-and-update or append a user row in the users tab."""
    sh = client.open_by_key(sheet_id)
    ws = sh.worksheet("users")
    records = ws.get_all_records()
    for i, record in enumerate(records):
        if record["user_id"] == user_id:
            ws.update_cell(i + 2, 2, display_name)  # row i+2: 1-indexed + header
            return
    ws.append_row([user_id, display_name, created_at])


def sheets_write_with_retry(fn, *args, **kwargs) -> None:
    """Call fn(*args, **kwargs), retry once on failure, log warning on second failure."""
    try:
        fn(*args, **kwargs)
    except Exception as e:
        logger.warning("Sheets write failed (%s), retrying in 1s...", e)
        time.sleep(1)
        try:
            fn(*args, **kwargs)
        except Exception as e2:
            logger.warning("Sheets write failed again (%s), skipping.", e2)
