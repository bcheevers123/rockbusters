"""Rockbusters game service — daily set selection and state management."""

import datetime
from typing import List

import pytz

from api.config import Config
from api.content_bank import RockbusterSet, get_enabled_sets

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


def get_todays_set(bank: List[RockbusterSet], config: Config) -> RockbusterSet:
    """Return today's RockbusterSet based on the configured timezone.

    Converts the current UTC time to *config.timezone*, extracts the local
    date, then delegates to :func:`get_set_for_date`.
    """
    tz = pytz.timezone(config.timezone)
    now_local = datetime.datetime.now(tz)
    today = now_local.date()
    return get_set_for_date(bank, today)
