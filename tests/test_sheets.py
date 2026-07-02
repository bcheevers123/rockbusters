"""Unit tests for api/sheets.py — all gspread calls are mocked."""

import sqlite3
from unittest.mock import MagicMock, patch

from api import sheets


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_client():
    return MagicMock()


def make_sheet_with_records(records):
    ws = MagicMock()
    ws.get_all_records.return_value = records
    return ws


# ---------------------------------------------------------------------------
# get_sheets_client
# ---------------------------------------------------------------------------

def test_get_sheets_client_calls_gspread():
    creds_json = '{"type": "service_account", "project_id": "x"}'
    with patch("api.sheets.gspread.service_account_from_dict") as mock_sa:
        mock_sa.return_value = MagicMock()
        client = sheets.get_sheets_client(creds_json)
    mock_sa.assert_called_once()
    assert client is not None


# ---------------------------------------------------------------------------
# load_all
# ---------------------------------------------------------------------------

def test_load_all_returns_three_tabs():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh

    sh.worksheet.side_effect = lambda name: make_sheet_with_records(
        [{"col": name}]
    )

    result = sheets.load_all(client, "SHEET_ID")

    assert set(result.keys()) == {"users", "guesses", "daily_reveals"}
    sh.worksheet.assert_any_call("users")
    sh.worksheet.assert_any_call("guesses")
    sh.worksheet.assert_any_call("daily_reveals")


# ---------------------------------------------------------------------------
# replay_into_db
# ---------------------------------------------------------------------------

def test_replay_into_db_inserts_users_guesses_reveals():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY);
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY, display_name TEXT, created_at TEXT
        );
        CREATE TABLE IF NOT EXISTS guesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL, set_id TEXT NOT NULL,
            clue_number INTEGER NOT NULL, is_correct INTEGER NOT NULL,
            guessed_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS daily_reveals (
            user_id TEXT NOT NULL, set_id TEXT NOT NULL, reveal_date TEXT NOT NULL,
            PRIMARY KEY (user_id, set_id)
        );
    """)

    data = {
        "users": [
            {"user_id": "u1", "display_name": "Alice", "created_at": "2026-01-01T00:00:00+00:00"},
        ],
        "guesses": [
            {"user_id": "u1", "set_id": "set-1", "clue_number": "1", "is_correct": "1", "guessed_at": "2026-01-01T00:00:00+00:00"},
        ],
        "daily_reveals": [
            {"user_id": "u1", "set_id": "set-1", "reveal_date": "2026-01-01"},
        ],
    }

    sheets.replay_into_db(conn, data)

    row = conn.execute("SELECT display_name FROM users WHERE user_id='u1'").fetchone()
    assert row[0] == "Alice"

    row = conn.execute("SELECT clue_number FROM guesses WHERE user_id='u1'").fetchone()
    assert row[0] == 1

    row = conn.execute("SELECT reveal_date FROM daily_reveals WHERE user_id='u1'").fetchone()
    assert row[0] == "2026-01-01"

    conn.close()


# ---------------------------------------------------------------------------
# append_guess
# ---------------------------------------------------------------------------

def test_append_guess_appends_correct_row():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws

    sheets.append_guess(client, "SHEET_ID", {
        "user_id": "u1",
        "set_id": "set-1",
        "clue_number": 2,
        "is_correct": 1,
        "guessed_at": "2026-01-01T00:00:00+00:00",
    })

    ws.append_row.assert_called_once_with(
        ["u1", "set-1", 2, 1, "2026-01-01T00:00:00+00:00"]
    )


# ---------------------------------------------------------------------------
# append_reveal
# ---------------------------------------------------------------------------

def test_append_reveal_appends_correct_row():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws

    sheets.append_reveal(client, "SHEET_ID", {
        "user_id": "u1",
        "set_id": "set-1",
        "reveal_date": "2026-01-01",
    })

    ws.append_row.assert_called_once_with(["u1", "set-1", "2026-01-01"])


# ---------------------------------------------------------------------------
# upsert_user_row — new user
# ---------------------------------------------------------------------------

def test_upsert_user_row_appends_when_user_not_found():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws
    ws.get_all_records.return_value = []  # no existing users

    sheets.upsert_user_row(client, "SHEET_ID", "u1", "Alice", "2026-01-01T00:00:00+00:00")

    ws.append_row.assert_called_once_with(["u1", "Alice", "2026-01-01T00:00:00+00:00"])


# ---------------------------------------------------------------------------
# upsert_user_row — existing user, display_name update
# ---------------------------------------------------------------------------

def test_upsert_user_row_updates_display_name_when_user_exists():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws
    # Row index 2 (1-indexed, row 1 = header)
    ws.get_all_records.return_value = [
        {"user_id": "u1", "display_name": "OldName", "created_at": "2026-01-01T00:00:00+00:00"}
    ]

    sheets.upsert_user_row(client, "SHEET_ID", "u1", "NewName", "2026-01-01T00:00:00+00:00")

    # Should update cell B2 (display_name column, row 2)
    ws.update_cell.assert_called_once_with(2, 2, "NewName")
    ws.append_row.assert_not_called()


# ---------------------------------------------------------------------------
# sheets_write_with_retry
# ---------------------------------------------------------------------------

def test_sheets_write_with_retry_succeeds_first_call():
    fn = MagicMock()
    sheets.sheets_write_with_retry(fn, "a", "b")
    fn.assert_called_once_with("a", "b")


def test_sheets_write_with_retry_retries_once_on_failure():
    fn = MagicMock(side_effect=[Exception("fail"), None])
    with patch("api.sheets.time.sleep"):
        sheets.sheets_write_with_retry(fn, "a")
    assert fn.call_count == 2


def test_sheets_write_with_retry_logs_warning_on_double_failure():
    fn = MagicMock(side_effect=Exception("fail"))
    with patch("api.sheets.time.sleep"), patch("api.sheets.logger.warning") as mock_warn:
        sheets.sheets_write_with_retry(fn, "a")  # must not raise
    assert mock_warn.call_count == 2
