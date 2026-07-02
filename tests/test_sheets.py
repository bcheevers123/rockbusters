"""Unit tests for api/sheets.py — all gspread calls are mocked."""

import sqlite3
from unittest.mock import MagicMock, call, patch

import pytest

from api.db import init_db
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

def test_get_sheets_client_calls_gspread(tmp_path):
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
    init_db(conn if False else ":memory:")  # use helper below
    conn = sqlite3.connect(":memory:")
    from api.db import init_db as _init
    _init(":memory:")
    # Use a fresh connection with init
    import tempfile, os
    tmp = tempfile.mktemp(suffix=".db")
    from api.db import init_db as real_init
    real_init(tmp)
    conn = sqlite3.connect(tmp)

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
    os.unlink(tmp)


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
