"""Tests for answer normalization and matching via check_answer."""

import pytest

from api.content_bank import Clue
from api.scoring import check_answer


@pytest.fixture
def wine_gums_clue():
    """Create a Wine Gums clue directly (sweetbusters-001 clue 1) without loading YAML."""
    return Clue(
        number=1,
        initials="W G",
        clue=(
            "Right, that bit in your mouth where the teeth sort of live, "
            "it's been on the red and white booze. What's happened there?"
        ),
        answer="Wine Gums",
        aliases=["wine gums", "winegums", "wine gum"],
        reasoning="gums (teeth live there) plus wine (red and white booze) = wine gums",
    )


def test_exact_match(wine_gums_clue):
    """Normalised exact match returns True."""
    assert check_answer(wine_gums_clue, "wine gums") is True


def test_whitespace_and_punctuation(wine_gums_clue):
    """Leading/trailing whitespace and punctuation is stripped before matching."""
    assert check_answer(wine_gums_clue, "  Wine Gums!! ") is True


def test_alias_match(wine_gums_clue):
    """A known alias (winegums, no space) returns True."""
    assert check_answer(wine_gums_clue, "winegums") is True


def test_wrong_answer_rejected(wine_gums_clue):
    """A completely different answer returns False."""
    assert check_answer(wine_gums_clue, "polo mints") is False


def test_empty_string_rejected(wine_gums_clue):
    """Empty string returns False without raising."""
    assert check_answer(wine_gums_clue, "") is False
