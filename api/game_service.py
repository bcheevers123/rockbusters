"""Rockbusters game service — daily set selection and state management."""

import datetime
from typing import List, Optional

import pytz

from api.config import Config
from api.content_bank import RockbusterSet, get_enabled_sets
from api.db import get_daily_override

# Fixed epoch for deterministic daily rotation
EPOCH = datetime.date(2026, 1, 1)


def get_set_for_date(bank: List[RockbusterSet], date: datetime.date) -> RockbusterSet:
    """Return the RockbusterSet scheduled for *date* using deterministic rotation.

    Filters the bank to enabled sets only, then picks the set at index
    ``(date - EPOCH).days % len(enabled)``.

    Raises:
        ValueError: if there are no enabled sets in the bank.
    """
    enabled = get_enabled_sets(bank)
    if not enabled:
        raise ValueError("No enabled sets in the content bank.")
    index = (date - EPOCH).days % len(enabled)
    return enabled[index]


def get_todays_set(
    bank: List[RockbusterSet],
    config: Config,
    conn=None,
) -> RockbusterSet:
    """Return today's RockbusterSet.

    If *conn* is provided, checks the daily_override table first. If a valid
    override exists and its set_id is in the enabled bank, returns that set.
    Otherwise falls back to date-based rotation.
    """
    tz = pytz.timezone(config.timezone)
    now_local = datetime.datetime.now(tz)
    today = now_local.date()
    today_str = today.strftime("%Y-%m-%d")

    if conn is not None:
        override_id = get_daily_override(conn, today_str)
        if override_id:
            enabled = get_enabled_sets(bank)
            match = next((s for s in enabled if s.id == override_id), None)
            if match:
                return match

    return get_set_for_date(bank, today)
