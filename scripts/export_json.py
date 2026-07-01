"""Rockbusters export script — converts the YAML question bank to JSON for the frontend."""

import json
import sys
from pathlib import Path

# Resolve paths relative to this script so the export works from any working directory
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from api.content_bank import get_enabled_sets, load_bank

BANK_PATH = ROOT / "data" / "rockbusters.yaml"
OUT_DIR = ROOT / "docs" / "data"
QUESTIONS_PATH = OUT_DIR / "rockbusters.json"
ANSWERS_PATH = OUT_DIR / "rockbusters-answers.json"


def set_to_questions_dict(rb_set) -> dict:
    """Serialise a RockbusterSet to a dict, stripping answer/aliases from clues."""
    return {
        "id": rb_set.id,
        "enabled": rb_set.enabled,
        "title": rb_set.title,
        "topic": rb_set.topic,
        "difficulty": rb_set.difficulty,
        "office_safe": rb_set.office_safe,
        "region_relevance": rb_set.region_relevance,
        "intro": rb_set.intro,
        "prize": rb_set.prize,
        "clues": [
            {
                "number": clue.number,
                "initials": clue.initials,
                "clue": clue.clue,
            }
            for clue in rb_set.clues
        ],
    }


def set_to_answers_dict(rb_set) -> dict:
    """Serialise a RockbusterSet to a dict with only answer/aliases/reasoning per clue."""
    return {
        "id": rb_set.id,
        "clues": [
            {
                "number": clue.number,
                "answer": clue.answer,
                "aliases": clue.aliases,
                "reasoning": clue.reasoning,
            }
            for clue in rb_set.clues
        ],
    }


def main():
    bank = load_bank(str(BANK_PATH))
    enabled = get_enabled_sets(bank)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    questions = [set_to_questions_dict(s) for s in enabled]
    answers = [set_to_answers_dict(s) for s in enabled]

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as fh:
        json.dump(questions, fh, indent=2, ensure_ascii=False)

    with open(ANSWERS_PATH, "w", encoding="utf-8") as fh:
        json.dump(answers, fh, indent=2, ensure_ascii=False)

    print(
        f"Exported {len(enabled)} sets to {QUESTIONS_PATH} and {ANSWERS_PATH}"
    )


if __name__ == "__main__":
    main()
