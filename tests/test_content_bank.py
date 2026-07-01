"""Tests for content bank loading and validation."""

import os
import tempfile

import pytest
import yaml

from api.content_bank import ContentBankError, load_bank


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _minimal_valid_set(set_id: str = "test-001") -> dict:
    """Return a minimal valid set dict."""
    return {
        "id": set_id,
        "enabled": True,
        "title": "Test Set",
        "topic": "testing",
        "difficulty": "easy",
        "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "A test set.",
        "prize": "A test prize.",
        "clues": [
            {
                "number": 1,
                "initials": "A B",
                "clue": "First clue.",
                "answer": "Answer One",
                "aliases": ["answer one"],
                "reasoning": "Because.",
            },
            {
                "number": 2,
                "initials": "C D",
                "clue": "Second clue.",
                "answer": "Answer Two",
                "aliases": ["answer two"],
                "reasoning": "Because.",
            },
            {
                "number": 3,
                "initials": "E F",
                "clue": "Third clue.",
                "answer": "Answer Three",
                "aliases": ["answer three"],
                "reasoning": "Because.",
            },
        ],
    }


def _write_yaml_to_temp(data: list) -> str:
    """Write *data* as YAML to a temp file and return the file path."""
    fh = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False, encoding="utf-8"
    )
    yaml.dump(data, fh, allow_unicode=True)
    fh.close()
    return fh.name


# ---------------------------------------------------------------------------
# Validation error tests
# ---------------------------------------------------------------------------

def test_missing_prize_raises_error():
    """A set with no 'prize' field raises ContentBankError."""
    bad_set = _minimal_valid_set()
    del bad_set["prize"]
    path = _write_yaml_to_temp([bad_set])
    try:
        with pytest.raises(ContentBankError, match="prize"):
            load_bank(path)
    finally:
        os.unlink(path)


def test_office_safe_false_raises_error():
    """A set with office_safe=False raises ContentBankError."""
    bad_set = _minimal_valid_set()
    bad_set["office_safe"] = False
    path = _write_yaml_to_temp([bad_set])
    try:
        with pytest.raises(ContentBankError, match="office_safe"):
            load_bank(path)
    finally:
        os.unlink(path)


def test_duplicate_id_raises_error():
    """Two sets with the same id raise ContentBankError."""
    set_a = _minimal_valid_set("dup-001")
    set_b = _minimal_valid_set("dup-001")
    path = _write_yaml_to_temp([set_a, set_b])
    try:
        with pytest.raises(ContentBankError, match="[Dd]uplicate"):
            load_bank(path)
    finally:
        os.unlink(path)


# ---------------------------------------------------------------------------
# Real file tests
# ---------------------------------------------------------------------------

def test_real_file_loads_three_sets():
    """The real data/rockbusters.yaml loads 3 sets successfully."""
    bank_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "rockbusters.yaml"
    )
    bank = load_bank(bank_path)
    assert len(bank) == 3


def test_real_file_each_set_has_three_clues():
    """Each set in the real YAML has exactly 3 clues."""
    bank_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "rockbusters.yaml"
    )
    bank = load_bank(bank_path)
    for rockbuster_set in bank:
        assert len(rockbuster_set.clues) == 3, (
            f"Set '{rockbuster_set.id}' has {len(rockbuster_set.clues)} clues, expected 3"
        )
