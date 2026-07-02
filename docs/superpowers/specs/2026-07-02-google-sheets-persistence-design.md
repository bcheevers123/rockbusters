# Google Sheets Persistence Design

**Date:** 2026-07-02  
**Status:** Approved

## Problem

Render free tier uses ephemeral storage — `/tmp/rockbusters.db` is lost on every spin-down. Users, scores, and guesses all reset. We need durable persistence without paying for a managed database.

## Solution: Sheets as append-only event log + in-memory SQLite

Google Sheets acts as the durable source of truth. On startup the app reads all rows from Sheets and replays them into an in-memory SQLite (`:memory:`). All runtime reads use fast SQL queries against in-memory SQLite. Every write goes to in-memory SQLite first, then appends/updates Sheets.

## Architecture

### New module: `api/sheets.py`

Owns all Google Sheets interaction. Exposes:

- `get_sheets_client(json_creds: str) -> gspread.Client` — authenticate via service account JSON
- `load_all(client, sheet_id) -> dict` — read all three tabs, return raw row lists
- `replay_into_db(conn, data)` — bulk-insert rows into an in-memory SQLite connection
- `append_guess(client, sheet_id, row)` — append one row to the `guesses` tab
- `append_reveal(client, sheet_id, row)` — append one row to the `daily_reveals` tab
- `upsert_user_row(client, sheet_id, user_id, display_name, created_at)` — find-and-update or append to `users` tab

### Changes to `api/main.py`

- On startup: if `GOOGLE_SHEETS_ID` env var is present, call `sheets.load_all()` + `sheets.replay_into_db()` to populate in-memory SQLite. If Sheets is unreachable, log error and continue with empty in-memory SQLite.
- `get_conn()` returns the shared in-memory connection when Sheets mode is active.
- After each successful `record_guess`, `record_reveal`, `upsert_user` call, fire the corresponding `sheets.*` write. One retry on failure; log warning and continue on second failure.

### Changes to `api/config.py`

Two new fields:
- `google_sheets_id: str` — from `GOOGLE_SHEETS_ID` env var (default `""`)
- `google_service_account_json: str` — from `GOOGLE_SERVICE_ACCOUNT_JSON` env var (default `""`)

Sheets mode is active when both are non-empty.

## Google Sheet structure

Three tabs (worksheets), each with a header row:

| Tab | Columns |
|-----|---------|
| `users` | user_id, display_name, created_at |
| `guesses` | user_id, set_id, clue_number, is_correct, guessed_at |
| `daily_reveals` | user_id, set_id, reveal_date |

## Error handling

- Sheets writes happen **after** SQLite write succeeds — SQLite is the fast path
- Failed Sheets write: retry once with 1s backoff, then log warning and return success to client
- Sheets unreachable on startup: log error, fall back to empty in-memory SQLite (app stays up)
- Rate limits: 60 writes/minute Google Sheets API limit — fine for small group usage

## New env vars

| Variable | Description |
|----------|-------------|
| `GOOGLE_SHEETS_ID` | Sheet ID from the URL (`/d/<ID>/edit`) |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Full service account JSON as a single-line string |

## New dependency

Add `gspread>=6.0` to `api/requirements.txt`.

## Testing

- Existing tests: unchanged — they use `:memory:` SQLite, no Sheets dependency
- New unit tests in `tests/test_sheets.py`: mock `gspread`, test `load_all`, `replay_into_db`, `append_guess`, `upsert_user_row`
- New integration smoke test (skipped unless `GOOGLE_SHEETS_ID` is set): verifies full startup rebuild round-trip

## Local development

No change — if `GOOGLE_SHEETS_ID` is not set, the app uses the SQLite file as before. Developers don't need Google credentials.
