"""Rockbusters content bank — loads and validates the YAML question bank."""

import re
from dataclasses import dataclass, field
from typing import List

import yaml


class ContentBankError(Exception):
    """Raised when the content bank YAML fails validation."""


@dataclass
class Clue:
    number: int
    initials: str
    clue: str
    answer: str
    aliases: List[str]
    reasoning: str


@dataclass
class RockbusterSet:
    id: str
    enabled: bool
    title: str
    topic: str
    difficulty: str
    office_safe: bool
    region_relevance: List[str]
    intro: str
    prize: str
    clues: List[Clue]


def normalize(text: str) -> str:
    """Lowercase, strip, collapse spaces, remove non-alphanumeric characters."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    text = re.sub(r" +", " ", text)
    return text


def load_bank(path: str) -> List[RockbusterSet]:
    """Parse and validate the YAML content bank. Returns a list of RockbusterSet objects.

    Raises ContentBankError on the first validation failure encountered.
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            raw = yaml.safe_load(fh)
    except FileNotFoundError:
        raise ContentBankError(f"Content bank file not found: {path}")
    except yaml.YAMLError as exc:
        raise ContentBankError(f"YAML parse error in {path}: {exc}")

    if not isinstance(raw, list):
        raise ContentBankError("Content bank must be a YAML list of sets.")

    seen_ids: set = set()
    result: List[RockbusterSet] = []

    for i, entry in enumerate(raw):
        label = f"set at index {i}"

        # id
        set_id = entry.get("id")
        if not set_id:
            raise ContentBankError(f"{label}: 'id' is required.")
        if set_id in seen_ids:
            raise ContentBankError(f"Duplicate id '{set_id}'.")
        seen_ids.add(set_id)
        label = f"set '{set_id}'"

        # required string fields
        for required_field in ("title", "topic", "prize"):
            if not entry.get(required_field):
                raise ContentBankError(f"{label}: '{required_field}' is required.")

        # office_safe must be boolean True
        office_safe = entry.get("office_safe")
        if office_safe is not True:
            raise ContentBankError(
                f"{label}: 'office_safe' must be boolean true (got {office_safe!r})."
            )

        # enabled must be boolean
        enabled = entry.get("enabled")
        if not isinstance(enabled, bool):
            raise ContentBankError(
                f"{label}: 'enabled' must be a boolean (got {enabled!r})."
            )

        # clues
        clues_raw = entry.get("clues")
        if not isinstance(clues_raw, list) or len(clues_raw) != 3:
            raise ContentBankError(f"{label}: exactly 3 clues are required.")

        clues: List[Clue] = []
        expected_numbers = {1, 2, 3}
        seen_numbers: set = set()

        for clue_raw in clues_raw:
            number = clue_raw.get("number")
            if number not in expected_numbers:
                raise ContentBankError(
                    f"{label}: clue numbers must be 1, 2, or 3 (got {number!r})."
                )
            if number in seen_numbers:
                raise ContentBankError(
                    f"{label}: duplicate clue number {number}."
                )
            seen_numbers.add(number)

            for required_clue_field in ("initials", "clue", "answer", "reasoning"):
                if not clue_raw.get(required_clue_field):
                    raise ContentBankError(
                        f"{label} clue {number}: '{required_clue_field}' is required."
                    )

            aliases: List[str] = list(clue_raw.get("aliases") or [])
            answer = clue_raw["answer"]
            normalized_answer = normalize(answer)
            normalized_aliases = [normalize(a) for a in aliases]
            if normalized_answer not in normalized_aliases:
                aliases.insert(0, normalized_answer)

            clues.append(
                Clue(
                    number=number,
                    initials=clue_raw["initials"],
                    clue=clue_raw["clue"],
                    answer=answer,
                    aliases=aliases,
                    reasoning=clue_raw["reasoning"],
                )
            )

        # sort clues by number for consistency
        clues.sort(key=lambda c: c.number)

        result.append(
            RockbusterSet(
                id=set_id,
                enabled=enabled,
                title=entry["title"],
                topic=entry["topic"],
                difficulty=entry.get("difficulty", "medium"),
                office_safe=office_safe,
                region_relevance=list(entry.get("region_relevance") or []),
                intro=entry.get("intro", ""),
                prize=entry["prize"],
                clues=clues,
            )
        )

    return result


def get_enabled_sets(bank: List[RockbusterSet]) -> List[RockbusterSet]:
    """Return only the sets with enabled=True."""
    return [s for s in bank if s.enabled]
