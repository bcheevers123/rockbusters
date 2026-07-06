"""Tests for daily set rotation logic."""

from datetime import date, timedelta

import pytest

from api.content_bank import Clue, RockbusterSet
from api.game_service import EPOCH, get_set_for_date


# ---------------------------------------------------------------------------
# Fixture: minimal in-memory bank (3 sets, no file I/O)
# ---------------------------------------------------------------------------

def _make_clues() -> list:
    """Return a minimal list of 3 Clue objects."""
    return [
        Clue(number=1, initials="A B", clue="Clue 1", answer="Ans1", aliases=["ans1"], reasoning="r"),
        Clue(number=2, initials="C D", clue="Clue 2", answer="Ans2", aliases=["ans2"], reasoning="r"),
        Clue(number=3, initials="E F", clue="Clue 3", answer="Ans3", aliases=["ans3"], reasoning="r"),
    ]


@pytest.fixture
def three_set_bank():
    """Three enabled RockbusterSet objects created directly without file I/O."""
    return [
        RockbusterSet(
            id="set-alpha",
            enabled=True,
            title="Alpha",
            topic="alpha",
            difficulty="easy",
            office_safe=True,
            region_relevance=["UK"],
            intro="",
            prize="Prize A",
            clues=_make_clues(),
        ),
        RockbusterSet(
            id="set-beta",
            enabled=True,
            title="Beta",
            topic="beta",
            difficulty="easy",
            office_safe=True,
            region_relevance=["UK"],
            intro="",
            prize="Prize B",
            clues=_make_clues(),
        ),
        RockbusterSet(
            id="set-gamma",
            enabled=True,
            title="Gamma",
            topic="gamma",
            difficulty="easy",
            office_safe=True,
            region_relevance=["UK"],
            intro="",
            prize="Prize C",
            clues=_make_clues(),
        ),
    ]


@pytest.fixture
def disabled_bank():
    """All sets have enabled=False."""
    sets = []
    for letter in ("X", "Y"):
        sets.append(
            RockbusterSet(
                id=f"set-{letter.lower()}",
                enabled=False,
                title=letter,
                topic=letter.lower(),
                difficulty="easy",
                office_safe=True,
                region_relevance=[],
                intro="",
                prize="nope",
                clues=_make_clues(),
            )
        )
    return sets


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_same_date_returns_same_set(three_set_bank):
    """Calling get_set_for_date twice with the same date always returns the same set."""
    d = date(2026, 1, 1)
    result_a = get_set_for_date(three_set_bank, d)
    result_b = get_set_for_date(three_set_bank, d)
    assert result_a.id == result_b.id


def test_consecutive_dates_return_different_sets(three_set_bank):
    """Day 1 and day 2 map to different sets (bank has 3 sets)."""
    day1 = get_set_for_date(three_set_bank, date(2026, 1, 1))
    day2 = get_set_for_date(three_set_bank, date(2026, 1, 2))
    assert day1.id != day2.id


def test_rotation_wraps_after_bank_length(three_set_bank):
    """After len(bank) days the rotation cycles back to day 0's set."""
    n = len(three_set_bank)  # 3
    day0 = get_set_for_date(three_set_bank, EPOCH)
    day_n = get_set_for_date(three_set_bank, EPOCH + timedelta(days=n))
    assert day0.id == day_n.id


def test_all_disabled_raises_value_error(disabled_bank):
    """A bank with no enabled sets raises ValueError."""
    with pytest.raises(ValueError, match="[Nn]o enabled sets"):
        get_set_for_date(disabled_bank, date(2026, 1, 1))


import sqlite3
from api.db import _create_schema, set_daily_override
from api.config import Config
from api.game_service import get_todays_set


def test_override_returns_pinned_set(three_set_bank):
    """When a daily override is set, get_todays_set returns the pinned set."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    _create_schema(conn)

    import datetime
    import pytz
    config = Config()
    tz = pytz.timezone(config.timezone)
    today_str = datetime.datetime.now(tz).strftime("%Y-%m-%d")

    set_daily_override(conn, "set-beta", today_str)

    result = get_todays_set(three_set_bank, config, conn=conn)
    assert result.id == "set-beta"
    conn.close()


def test_override_unknown_id_falls_back_to_rotation(three_set_bank):
    """When the override set_id doesn't exist in the bank, fall back to rotation."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    _create_schema(conn)

    import datetime
    import pytz
    config = Config()
    tz = pytz.timezone(config.timezone)
    today_str = datetime.datetime.now(tz).strftime("%Y-%m-%d")

    set_daily_override(conn, "nonexistent-set-999", today_str)

    # Should fall back to rotation without raising
    result = get_todays_set(three_set_bank, config, conn=conn)
    assert result.id in {s.id for s in three_set_bank}
    conn.close()


def test_no_conn_uses_rotation(three_set_bank):
    """With conn=None, get_todays_set uses date rotation as before."""
    config = Config()
    result = get_todays_set(three_set_bank, config, conn=None)
    assert result.id in {s.id for s in three_set_bank}
