"""Tests for database scoring functions using in-memory SQLite."""

import os
import sqlite3
import tempfile

import pytest

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


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------

@pytest.fixture
def conn():
    """Return an open SQLite connection with the schema initialised by init_db.

    Uses a temporary file so that init_db and the connection share the same
    database state — no DDL duplication required.
    """
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    init_db(db_path)
    c = sqlite3.connect(db_path)
    c.row_factory = sqlite3.Row
    yield c
    c.close()
    os.unlink(db_path)


# ---------------------------------------------------------------------------
# has_correct_guess / record_guess
# ---------------------------------------------------------------------------

def test_has_correct_guess_false_before_record(conn):
    """has_correct_guess returns False before any guess is recorded."""
    assert has_correct_guess(conn, "user1", "set-alpha", 1) is False


def test_has_correct_guess_true_after_correct_record(conn):
    """has_correct_guess returns True after a correct guess is recorded."""
    upsert_user(conn, "user1", "User One")
    record_guess(conn, "user1", "set-alpha", 1, is_correct=True)
    assert has_correct_guess(conn, "user1", "set-alpha", 1) is True


# ---------------------------------------------------------------------------
# has_revealed / record_reveal
# ---------------------------------------------------------------------------

def test_has_revealed_false_before_record(conn):
    """has_revealed returns False before record_reveal is called."""
    assert has_revealed(conn, "user2", "set-alpha") is False


def test_has_revealed_true_after_record(conn):
    """has_revealed returns True after record_reveal is called."""
    upsert_user(conn, "user2", "User Two")
    record_reveal(conn, "user2", "set-alpha", "2026-01-01")
    assert has_revealed(conn, "user2", "set-alpha") is True


# ---------------------------------------------------------------------------
# get_user_score_today
# ---------------------------------------------------------------------------

def test_get_user_score_today_correct_count(conn):
    """get_user_score_today returns the number of correct guesses for a user+set."""
    upsert_user(conn, "user3", "User Three")
    record_guess(conn, "user3", "set-alpha", 1, is_correct=True)
    record_guess(conn, "user3", "set-alpha", 2, is_correct=True)
    record_guess(conn, "user3", "set-alpha", 3, is_correct=False)
    assert get_user_score_today(conn, "user3", "set-alpha") == 2


def test_get_user_score_today_zero_for_no_guesses(conn):
    """get_user_score_today returns 0 for a user who has never guessed."""
    assert get_user_score_today(conn, "ghost-user", "set-alpha") == 0


# ---------------------------------------------------------------------------
# get_leaderboard
# ---------------------------------------------------------------------------

def test_leaderboard_sorted_descending(conn):
    """get_leaderboard returns rows sorted by total_points descending."""
    upsert_user(conn, "player-a", "Player A")
    upsert_user(conn, "player-b", "Player B")
    upsert_user(conn, "player-c", "Player C")

    # player-b gets 3 correct, player-a gets 1, player-c gets 0
    record_guess(conn, "player-a", "set-alpha", 1, is_correct=True)
    record_guess(conn, "player-b", "set-alpha", 1, is_correct=True)
    record_guess(conn, "player-b", "set-alpha", 2, is_correct=True)
    record_guess(conn, "player-b", "set-alpha", 3, is_correct=True)

    rows = get_leaderboard(conn)
    points = [r["total_points"] for r in rows]
    assert points == sorted(points, reverse=True)
    assert rows[0]["user_id"] == "player-b"


# ---------------------------------------------------------------------------
# upsert_user idempotency
# ---------------------------------------------------------------------------

def test_upsert_user_idempotent(conn):
    """upsert_user can be called twice for the same user_id without error."""
    upsert_user(conn, "idempotent-user", "Old Name")
    upsert_user(conn, "idempotent-user", "New Name")
    # Should not raise; verify the name was updated
    row = conn.execute(
        "SELECT display_name FROM users WHERE user_id = ?", ("idempotent-user",)
    ).fetchone()
    assert row is not None
    assert row[0] == "New Name"
