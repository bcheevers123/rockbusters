"""Tests for daily_override DB helpers."""

import sqlite3
import pytest
from api.db import _create_schema, get_daily_override, set_daily_override


@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.row_factory = sqlite3.Row
    _create_schema(c)
    yield c
    c.close()


def test_get_daily_override_empty(conn):
    """Returns None when no override row exists."""
    assert get_daily_override(conn, "2026-07-06") is None


def test_set_and_get_daily_override(conn):
    """set then get returns the set_id for matching date."""
    set_daily_override(conn, "sweetbusters-001", "2026-07-06")
    assert get_daily_override(conn, "2026-07-06") == "sweetbusters-001"


def test_override_different_date_returns_none(conn):
    """Override for a different date returns None."""
    set_daily_override(conn, "sweetbusters-001", "2026-07-05")
    assert get_daily_override(conn, "2026-07-06") is None


def test_set_override_replaces_existing(conn):
    """Writing a second override replaces the first."""
    set_daily_override(conn, "sweetbusters-001", "2026-07-06")
    set_daily_override(conn, "filmbusters-002", "2026-07-06")
    assert get_daily_override(conn, "2026-07-06") == "filmbusters-002"
