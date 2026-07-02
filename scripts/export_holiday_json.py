"""Export holiday sets YAML to JSON for the frontend."""

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
HOLIDAY_PATH = ROOT / "data" / "holiday-sets.yaml"
OUT_DIR = ROOT / "docs" / "data"
QUESTIONS_PATH = OUT_DIR / "holiday-sets.json"
ANSWERS_PATH = OUT_DIR / "holiday-answers.json"


def main():
    with open(HOLIDAY_PATH, encoding="utf-8") as f:
        sets = yaml.safe_load(f)

    questions = []
    answers = []

    for s in sets:
        clues_q = []
        clues_a = []
        for i, c in enumerate(s["clues"], 1):
            num = c.get("number", i)
            clues_q.append({
                "number": num,
                "initials": c["initials"],
                "clue": c["clue"],
            })
            aliases = list(c.get("aliases") or [])
            answer_norm = c["answer"].lower().strip()
            if answer_norm not in aliases:
                aliases.insert(0, answer_norm)
            clues_a.append({
                "number": num,
                "answer": c["answer"],
                "aliases": aliases,
                "reasoning": c.get("reasoning", ""),
            })

        questions.append({
            "id": s["id"],
            "enabled": True,
            "title": s.get("title", s["id"]),
            "topic": s["id"].rsplit("-", 1)[0],
            "difficulty": s.get("difficulty", "medium"),
            "office_safe": True,
            "region_relevance": [],
            "intro": s.get("intro", ""),
            "prize": s.get("prize", ""),
            "clues": clues_q,
        })
        answers.append({
            "id": s["id"],
            "clues": clues_a,
        })

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    with open(ANSWERS_PATH, "w", encoding="utf-8") as f:
        json.dump(answers, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(questions)} holiday sets to {QUESTIONS_PATH}")


if __name__ == "__main__":
    main()
