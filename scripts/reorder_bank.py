"""
Rebuild rockbusters.yaml:
  - Keep the first 20 sets per category (drop extras)
  - Interleave so the same category never appears within MIN_GAP positions
  - Use a deterministic seed so the order is stable across runs
  - Write back to data/rockbusters.yaml
"""

import random
import sys
from collections import defaultdict, deque
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
BANK_PATH = ROOT / "data" / "rockbusters.yaml"
MIN_GAP = 3   # category must wait this many slots before reappearing
SEED = 42
MAX_PER_CAT = 20


def category(s):
    return s["id"].rsplit("-", 1)[0]


def interleave(groups: dict[str, list]) -> list:
    """
    Round-robin with a gap constraint.
    Uses a ready-queue and a cooling-down deque to ensure no category
    repeats within MIN_GAP positions.
    """
    rng = random.Random(SEED)

    # Shuffle within each group so we don't always pick -001, -002... in order
    pools = {}
    for cat, items in groups.items():
        pool = items[:]
        rng.shuffle(pool)
        pools[cat] = deque(pool)

    result = []
    # categories available to pick from right now
    ready = list(pools.keys())
    rng.shuffle(ready)
    ready = deque(ready)
    # cooling[(cat, reinsert_at_index)] — we reinsert when len(result) >= reinsert_at
    cooling = []

    while any(pools[c] for c in pools):
        # Move any cooled-off categories back into ready
        still_cooling = []
        for cat, reinsert_at in cooling:
            if len(result) >= reinsert_at and pools[cat]:
                ready.append(cat)
            else:
                still_cooling.append((cat, reinsert_at))
        cooling = still_cooling

        # Find the first ready category that still has items
        chosen = None
        skipped = []
        while ready:
            candidate = ready.popleft()
            if pools[candidate]:
                chosen = candidate
                break
            # exhausted — drop it

        if chosen is None:
            # All ready categories exhausted; forced to pull from cooling early
            if not cooling:
                break
            cooling.sort(key=lambda x: x[1])
            cat, _ = cooling.pop(0)
            if pools[cat]:
                chosen = cat
            else:
                continue

        item = pools[chosen].popleft()
        result.append(item)

        # Put back any skipped categories
        ready.extendleft(reversed(skipped))

        # Send chosen to cooling
        reinsert_at = len(result) + MIN_GAP
        if pools[chosen]:
            cooling.append((chosen, reinsert_at))

    return result


def main():
    with open(BANK_PATH, encoding="utf-8") as f:
        all_sets = yaml.safe_load(f)

    # Group by category, keep first MAX_PER_CAT
    by_cat = defaultdict(list)
    for s in all_sets:
        cat = category(s)
        by_cat[cat].append(s)

    groups = {cat: items[:MAX_PER_CAT] for cat, items in by_cat.items()}

    total_in = sum(len(v) for v in groups.values())
    print(f"Categories: {len(groups)}, sets after trim: {total_in}")

    ordered = interleave(groups)
    print(f"Sets in output: {len(ordered)}")

    # Verify gap constraint
    violations = 0
    recent = deque(maxlen=MIN_GAP)
    for s in ordered:
        cat = category(s)
        if cat in recent:
            violations += 1
            print(f"  GAP VIOLATION: {cat} at position {ordered.index(s)}")
        recent.append(cat)
    if violations == 0:
        print(f"Gap constraint satisfied (min gap = {MIN_GAP})")
    else:
        print(f"{violations} gap violations — check interleave logic")
        sys.exit(1)

    with open(BANK_PATH, "w", encoding="utf-8") as f:
        yaml.dump(ordered, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"Written to {BANK_PATH}")


if __name__ == "__main__":
    main()
