# Dev Panel: Browse, Random & Set as Today — Design Spec

**Date:** 2026-07-06  
**Status:** Approved

---

## Overview

Three related changes:

1. **Dev panel Browse modal** — lets the dev browse all question sets by name and preview or set any of them as today's quiz.
2. **"Set as Today" server-side override** — a passcode-gated API endpoint that pins a specific set for the current local date, expiring automatically at midnight. Affects all users.
3. **Em dash cleanup** — removes all em dashes from the question bank YAML files, replacing them with grammatically correct alternatives.

---

## 1. Backend: Daily Override

### DB schema

Add a `daily_override` table to the SQLite schema (both file and in-memory modes):

```sql
CREATE TABLE IF NOT EXISTS daily_override (
    set_id    TEXT NOT NULL,
    valid_date TEXT NOT NULL
);
```

Single logical row — always replaced on write (DELETE then INSERT). `valid_date` is stored as `YYYY-MM-DD` in the configured timezone.

### `api/db.py` additions

- `get_daily_override(conn) -> str | None` — returns the `set_id` if `valid_date` matches today's local date string, else `None`.
- `set_daily_override(conn, set_id: str, date_str: str)` — deletes all rows then inserts one.
- Schema migration: `_create_schema` extended with the new `CREATE TABLE IF NOT EXISTS` statement.

### `api/game_service.py` changes

`get_todays_set(bank, config, conn=None)` gains an optional `conn` parameter:

1. If `conn` is provided, call `get_daily_override(conn)`.
2. If an override set_id is returned and that id exists among enabled sets, return it.
3. Otherwise fall back to the existing date-based rotation.

`get_todays_set` is also called from `get_set_for_date` indirectly — only the top-level function needs the conn; internal rotation logic is unchanged.

### New API endpoints

**`POST /api/admin/set-today?set_id=XYZ&secret=...`**

- Validates passcode (same SHA-256 hash as `/api/admin/reset-leaderboard`).
- Validates `set_id` exists in the loaded bank (enabled sets only).
- Writes override row for today's local date.
- Returns `{"ok": true, "set_id": "XYZ"}`.
- Returns 403 on bad passcode, 404 if set_id not found in enabled bank.

**`GET /api/bank`**

- Returns all enabled sets as a list: `[{"id": "...", "title": "...", "topic": "..."}]`.
- No authentication required (question titles are not sensitive).
- Used by the frontend Browse modal.

### `/api/today` update

Pass `conn` into `get_todays_set` so the override is respected on every load.

---

## 2. Frontend: Dev Panel Changes

### Dev panel bar

The existing bar layout gains two new buttons between "Next →" and "Today":

```
Dev  [← Prev]  <set-info>  [Next →]  [Browse]  [Random]  [Today]  [Reset LB]  [Lock]
```

- **Browse** — opens the Browse modal.
- **Random** — picks a random enabled set from the bank (fetched via `GET /api/bank`), loads it locally as a preview immediately (uses existing offset mechanism to display the matching set).

### Browse modal

A full-screen semi-transparent overlay (same no-framework DOM approach as the rest of the app). Structure:

- Header row: title "Browse Sets", a **Random** button (selects a random row in the list), and a close button.
- Scrollable list of all enabled sets from `GET /api/bank`, grouped by `topic`. Each row shows `id` and `title`. Clicking a row selects it (highlighted).
- Footer: **Preview** button (loads selected set locally, closes modal) and **Set as Today** button (prompts for passcode, calls `POST /api/admin/set-today`, reloads quiz for all users, closes modal).

**"Set as Today" flow:**
1. `window.prompt('Dev passcode:')` — same UX as existing reset-leaderboard.
2. `POST /api/admin/set-today?set_id=...&secret=...`
3. On success: close modal, call `loadQuiz()`.
4. On failure: `window.alert(error)`.

**"Preview" flow:**
- Calculate what offset value would make the selected set appear today in the local rotation (by iterating enabled sets and finding the index).
- Call `devSetOffset(calculatedOffset)` then `loadQuiz()`.
- Does not require a passcode; purely local/temporary.

### Bank caching

`GET /api/bank` is fetched once when the Browse modal is first opened and cached in a module-level variable `_bankSets`. Subsequent opens reuse the cache.

---

## 3. Em Dash Cleanup

### Scope

341 em dash occurrences across 42 of the 92 batch YAML files in `data/batches/`. They appear in `clue`, `intro`, `reasoning`, and `prize` fields.

### Approach

An AI-assisted pass over each affected file:
- Em dash as **parenthetical aside** (` — X — `) → rewrite as `, X,` or `(X)`.
- Em dash as **clause break** (` — `) mid-sentence → `, ` or `. ` depending on what reads naturally.
- Em dash as **trailing pause/afterthought** → `. ` or remove.

All rewrites must preserve meaning, tone (Karl Pilkington voice), and phonetic validity of clues.

### Validation

After rewriting, run `python -c "from api.content_bank import load_bank; load_bank('data/rockbusters.yaml')"` to confirm no YAML breaks and no validation errors.

### Regeneration

After batch files are cleaned:
1. Regenerate `data/rockbusters.yaml` from batches (via existing merge/export scripts).
2. Regenerate `docs/data/rockbusters.json` and `docs/data/rockbusters-answers.json`.

---

## Out of Scope

- Holiday sets (`data/holiday-sets.yaml`) — em dash cleanup applies to main bank only unless explicitly requested.
- Persistent override across server restarts — override is in-memory/SQLite and intentionally ephemeral.
- Override UI for non-dev users — this feature is passcode-gated throughout.
