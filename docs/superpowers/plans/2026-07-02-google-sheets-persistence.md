# Google Sheets Persistence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace ephemeral SQLite on Render free tier with Google Sheets as durable event log, replayed into in-memory SQLite on startup.

**Architecture:** A new `api/sheets.py` module owns all Sheets interaction. On startup, if `GOOGLE_SHEETS_ID` and `GOOGLE_SERVICE_ACCOUNT_JSON` env vars are set, the app reads all three Sheets tabs and bulk-inserts them into an in-memory SQLite. All runtime reads hit in-memory SQLite (fast SQL joins). Every write goes to SQLite first, then appends/updates Sheets with one retry. Locally, without the env vars, nothing changes.

**Tech Stack:** Python 3, FastAPI, gspread>=6.0, SQLite `:memory:`, pytest, unittest.mock

## Global Constraints

- `gspread>=6.0` — minimum version
- Sheets mode active only when both `GOOGLE_SHEETS_ID` and `GOOGLE_SERVICE_ACCOUNT_JSON` are non-empty strings
- Sheets writes happen **after** SQLite write succeeds — SQLite is the fast path
- Failed Sheets write: retry once with 1s sleep, log warning on second failure, return success to client
- Startup Sheets failure: log error, fall back to empty in-memory SQLite, app stays up
- Existing tests must pass unchanged
- Run all tests from repo root: `pytest tests/ -v`

---

### Task 1: Add gspread dependency and new config fields

**Files:**
- Modify: `api/requirements.txt`
- Modify: `api/config.py`

**Interfaces:**
- Produces: `Config.google_sheets_id: str`, `Config.google_service_account_json: str`, `Config.sheets_enabled() -> bool`

- [ ] **Step 1: Add gspread to requirements**

Open `api/requirements.txt`. It currently contains:
```
fastapi>=0.111
uvicorn[standard]>=0.29
python-dotenv>=1.0
pyyaml>=6.0
pytz>=2024.1
```

Add one line:
```
gspread>=6.0
```

- [ ] **Step 2: Add two new fields and a helper to Config**

Open `api/config.py`. The current `Config` dataclass ends at `api_secret`. Add two new fields and a method:

```python
    google_sheets_id: str = field(
        default_factory=lambda: os.getenv("GOOGLE_SHEETS_ID", "")
    )
    google_service_account_json: str = field(
        default_factory=lambda: os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    )

    def sheets_enabled(self) -> bool:
        return bool(self.google_sheets_id and self.google_service_account_json)
```

- [ ] **Step 3: Install the new dependency**

```bash
pip install gspread>=6.0
```

Expected: installs without error.

- [ ] **Step 4: Verify existing tests still pass**

```bash
pytest tests/ -v
```

Expected: all existing tests pass, no import errors.

- [ ] **Step 5: Commit**

```bash
git add api/requirements.txt api/config.py
git commit -m "feat: add gspread dependency and Sheets config fields"
```

---

### Task 2: Implement api/sheets.py

**Files:**
- Create: `api/sheets.py`

**Interfaces:**
- Consumes: `Config.google_service_account_json: str`, `Config.google_sheets_id: str`
- Produces:
  - `get_sheets_client(json_creds: str) -> gspread.Client`
  - `load_all(client: gspread.Client, sheet_id: str) -> dict` — returns `{"users": [...], "guesses": [...], "daily_reveals": [...]}`; each value is a list of dicts (header row as keys)
  - `replay_into_db(conn: sqlite3.Connection, data: dict) -> None`
  - `append_guess(client: gspread.Client, sheet_id: str, row: dict) -> None` — row keys: user_id, set_id, clue_number, is_correct, guessed_at
  - `append_reveal(client: gspread.Client, sheet_id: str, row: dict) -> None` — row keys: user_id, set_id, reveal_date
  - `upsert_user_row(client: gspread.Client, sheet_id: str, user_id: str, display_name: str, created_at: str) -> None`

- [ ] **Step 1: Write failing tests for sheets.py**

Create `tests/test_sheets.py`:

```python
"""Unit tests for api/sheets.py — all gspread calls are mocked."""

import sqlite3
from unittest.mock import MagicMock, call, patch

import pytest

from api.db import init_db
from api import sheets


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_client():
    return MagicMock()


def make_sheet_with_records(records):
    ws = MagicMock()
    ws.get_all_records.return_value = records
    return ws


# ---------------------------------------------------------------------------
# get_sheets_client
# ---------------------------------------------------------------------------

def test_get_sheets_client_calls_gspread(tmp_path):
    creds_json = '{"type": "service_account", "project_id": "x"}'
    with patch("api.sheets.gspread.service_account_from_dict") as mock_sa:
        mock_sa.return_value = MagicMock()
        client = sheets.get_sheets_client(creds_json)
    mock_sa.assert_called_once()
    assert client is not None


# ---------------------------------------------------------------------------
# load_all
# ---------------------------------------------------------------------------

def test_load_all_returns_three_tabs():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh

    sh.worksheet.side_effect = lambda name: make_sheet_with_records(
        [{"col": name}]
    )

    result = sheets.load_all(client, "SHEET_ID")

    assert set(result.keys()) == {"users", "guesses", "daily_reveals"}
    sh.worksheet.assert_any_call("users")
    sh.worksheet.assert_any_call("guesses")
    sh.worksheet.assert_any_call("daily_reveals")


# ---------------------------------------------------------------------------
# replay_into_db
# ---------------------------------------------------------------------------

def test_replay_into_db_inserts_users_guesses_reveals():
    conn = sqlite3.connect(":memory:")
    init_db(conn if False else ":memory:")  # use helper below
    conn = sqlite3.connect(":memory:")
    from api.db import init_db as _init
    _init(":memory:")
    # Use a fresh connection with init
    import tempfile, os
    tmp = tempfile.mktemp(suffix=".db")
    from api.db import init_db as real_init
    real_init(tmp)
    conn = sqlite3.connect(tmp)

    data = {
        "users": [
            {"user_id": "u1", "display_name": "Alice", "created_at": "2026-01-01T00:00:00+00:00"},
        ],
        "guesses": [
            {"user_id": "u1", "set_id": "set-1", "clue_number": "1", "is_correct": "1", "guessed_at": "2026-01-01T00:00:00+00:00"},
        ],
        "daily_reveals": [
            {"user_id": "u1", "set_id": "set-1", "reveal_date": "2026-01-01"},
        ],
    }

    sheets.replay_into_db(conn, data)

    row = conn.execute("SELECT display_name FROM users WHERE user_id='u1'").fetchone()
    assert row[0] == "Alice"

    row = conn.execute("SELECT clue_number FROM guesses WHERE user_id='u1'").fetchone()
    assert row[0] == 1

    row = conn.execute("SELECT reveal_date FROM daily_reveals WHERE user_id='u1'").fetchone()
    assert row[0] == "2026-01-01"

    conn.close()
    os.unlink(tmp)


# ---------------------------------------------------------------------------
# append_guess
# ---------------------------------------------------------------------------

def test_append_guess_appends_correct_row():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws

    sheets.append_guess(client, "SHEET_ID", {
        "user_id": "u1",
        "set_id": "set-1",
        "clue_number": 2,
        "is_correct": 1,
        "guessed_at": "2026-01-01T00:00:00+00:00",
    })

    ws.append_row.assert_called_once_with(
        ["u1", "set-1", 2, 1, "2026-01-01T00:00:00+00:00"]
    )


# ---------------------------------------------------------------------------
# append_reveal
# ---------------------------------------------------------------------------

def test_append_reveal_appends_correct_row():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws

    sheets.append_reveal(client, "SHEET_ID", {
        "user_id": "u1",
        "set_id": "set-1",
        "reveal_date": "2026-01-01",
    })

    ws.append_row.assert_called_once_with(["u1", "set-1", "2026-01-01"])


# ---------------------------------------------------------------------------
# upsert_user_row — new user
# ---------------------------------------------------------------------------

def test_upsert_user_row_appends_when_user_not_found():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws
    ws.get_all_records.return_value = []  # no existing users

    sheets.upsert_user_row(client, "SHEET_ID", "u1", "Alice", "2026-01-01T00:00:00+00:00")

    ws.append_row.assert_called_once_with(["u1", "Alice", "2026-01-01T00:00:00+00:00"])


# ---------------------------------------------------------------------------
# upsert_user_row — existing user, display_name update
# ---------------------------------------------------------------------------

def test_upsert_user_row_updates_display_name_when_user_exists():
    client = make_client()
    sh = MagicMock()
    client.open_by_key.return_value = sh
    ws = MagicMock()
    sh.worksheet.return_value = ws
    # Row index 2 (1-indexed, row 1 = header)
    ws.get_all_records.return_value = [
        {"user_id": "u1", "display_name": "OldName", "created_at": "2026-01-01T00:00:00+00:00"}
    ]

    sheets.upsert_user_row(client, "SHEET_ID", "u1", "NewName", "2026-01-01T00:00:00+00:00")

    # Should update cell B2 (display_name column, row 2)
    ws.update_cell.assert_called_once_with(2, 2, "NewName")
    ws.append_row.assert_not_called()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_sheets.py -v
```

Expected: `ModuleNotFoundError: No module named 'api.sheets'` or similar — all tests fail.

- [ ] **Step 3: Implement api/sheets.py**

Create `api/sheets.py`:

```python
"""Google Sheets persistence layer for Rockbusters."""

import json
import logging
import sqlite3
import time

import gspread
from google.oauth2.service_account import Credentials

logger = logging.getLogger(__name__)

_SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]


def get_sheets_client(json_creds: str) -> gspread.Client:
    """Authenticate with a service account JSON string and return a gspread client."""
    creds_dict = json.loads(json_creds)
    creds = Credentials.from_service_account_info(creds_dict, scopes=_SCOPES)
    return gspread.authorize(creds)


def load_all(client: gspread.Client, sheet_id: str) -> dict:
    """Read all three tabs from the sheet. Returns dict with keys: users, guesses, daily_reveals."""
    sh = client.open_by_key(sheet_id)
    return {
        "users": sh.worksheet("users").get_all_records(),
        "guesses": sh.worksheet("guesses").get_all_records(),
        "daily_reveals": sh.worksheet("daily_reveals").get_all_records(),
    }


def replay_into_db(conn: sqlite3.Connection, data: dict) -> None:
    """Bulk-insert all rows from Sheets data into an already-initialised SQLite connection."""
    for row in data.get("users", []):
        conn.execute(
            "INSERT OR IGNORE INTO users (user_id, display_name, created_at) VALUES (?, ?, ?)",
            (row["user_id"], row["display_name"], row["created_at"]),
        )

    for row in data.get("guesses", []):
        conn.execute(
            """
            INSERT INTO guesses (user_id, set_id, clue_number, is_correct, guessed_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                row["user_id"],
                row["set_id"],
                int(row["clue_number"]),
                int(row["is_correct"]),
                row["guessed_at"],
            ),
        )

    for row in data.get("daily_reveals", []):
        conn.execute(
            "INSERT OR IGNORE INTO daily_reveals (user_id, set_id, reveal_date) VALUES (?, ?, ?)",
            (row["user_id"], row["set_id"], row["reveal_date"]),
        )

    conn.commit()


def append_guess(client: gspread.Client, sheet_id: str, row: dict) -> None:
    """Append one guess row to the guesses tab."""
    sh = client.open_by_key(sheet_id)
    ws = sh.worksheet("guesses")
    ws.append_row([
        row["user_id"],
        row["set_id"],
        row["clue_number"],
        row["is_correct"],
        row["guessed_at"],
    ])


def append_reveal(client: gspread.Client, sheet_id: str, row: dict) -> None:
    """Append one reveal row to the daily_reveals tab."""
    sh = client.open_by_key(sheet_id)
    ws = sh.worksheet("daily_reveals")
    ws.append_row([row["user_id"], row["set_id"], row["reveal_date"]])


def upsert_user_row(
    client: gspread.Client,
    sheet_id: str,
    user_id: str,
    display_name: str,
    created_at: str,
) -> None:
    """Find-and-update or append a user row in the users tab."""
    sh = client.open_by_key(sheet_id)
    ws = sh.worksheet("users")
    records = ws.get_all_records()
    for i, record in enumerate(records):
        if record["user_id"] == user_id:
            ws.update_cell(i + 2, 2, display_name)  # row i+2: 1-indexed + header
            return
    ws.append_row([user_id, display_name, created_at])


def sheets_write_with_retry(fn, *args, **kwargs) -> None:
    """Call fn(*args, **kwargs), retry once on failure, log warning on second failure."""
    try:
        fn(*args, **kwargs)
    except Exception as e:
        logger.warning("Sheets write failed (%s), retrying in 1s...", e)
        time.sleep(1)
        try:
            fn(*args, **kwargs)
        except Exception as e2:
            logger.warning("Sheets write failed again (%s), skipping.", e2)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_sheets.py -v
```

Expected: all 7 tests pass.

- [ ] **Step 5: Run full test suite to check nothing broke**

```bash
pytest tests/ -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit**

```bash
git add api/sheets.py tests/test_sheets.py
git commit -m "feat: implement sheets.py — Sheets client, load, replay, append, upsert"
```

---

### Task 3: Wire sheets.py into main.py

**Files:**
- Modify: `api/main.py`

**Interfaces:**
- Consumes:
  - `Config.sheets_enabled() -> bool`
  - `Config.google_sheets_id: str`
  - `Config.google_service_account_json: str`
  - `sheets.get_sheets_client(json_creds: str) -> gspread.Client`
  - `sheets.load_all(client, sheet_id) -> dict`
  - `sheets.replay_into_db(conn, data) -> None`
  - `sheets.append_guess(client, sheet_id, row: dict) -> None`
  - `sheets.append_reveal(client, sheet_id, row: dict) -> None`
  - `sheets.upsert_user_row(client, sheet_id, user_id, display_name, created_at) -> None`
  - `sheets.sheets_write_with_retry(fn, *args, **kwargs) -> None`

- [ ] **Step 1: Write failing test for Sheets-mode startup (mocked)**

Add to `tests/test_api.py` — append after the existing tests:

```python
# ---------------------------------------------------------------------------
# Sheets mode: startup rebuild test (mocked)
# ---------------------------------------------------------------------------

def test_sheets_mode_leaderboard_uses_replayed_data(tmp_path):
    """When Sheets env vars are set, startup replays Sheets data into in-memory SQLite.
    The leaderboard endpoint should return data from the replayed db."""
    import importlib
    import sys
    from unittest.mock import MagicMock, patch

    bank_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "data", "rockbusters.yaml")
    )

    # Remove cached api modules
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]

    fake_sheets_data = {
        "users": [{"user_id": "u99", "display_name": "SheetUser", "created_at": "2026-01-01T00:00:00+00:00"}],
        "guesses": [
            {"user_id": "u99", "set_id": "any-set", "clue_number": "1", "is_correct": "1", "guessed_at": "2026-01-01T00:00:00+00:00"},
            {"user_id": "u99", "set_id": "any-set", "clue_number": "2", "is_correct": "1", "guessed_at": "2026-01-01T00:00:00+00:00"},
        ],
        "daily_reveals": [],
    }

    mock_client = MagicMock()

    os.environ["GOOGLE_SHEETS_ID"] = "FAKE_SHEET_ID"
    os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"] = '{"type":"service_account"}'
    os.environ["ROCKBUSTERS_BANK_PATH"] = bank_path
    # No SQLITE_PATH — should use in-memory

    with patch("api.sheets.get_sheets_client", return_value=mock_client), \
         patch("api.sheets.load_all", return_value=fake_sheets_data):
        from api.main import app
        from fastapi.testclient import TestClient
        with TestClient(app) as c:
            resp = c.get("/api/leaderboard")
            assert resp.status_code == 200
            names = [e["display_name"] for e in resp.json()["leaderboard"]]
            assert "SheetUser" in names

    # Cleanup
    del os.environ["GOOGLE_SHEETS_ID"]
    del os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]
```

- [ ] **Step 2: Run new test to verify it fails**

```bash
pytest tests/test_api.py::test_sheets_mode_leaderboard_uses_replayed_data -v
```

Expected: FAIL — `Config` has no `sheets_enabled`, or startup ignores Sheets env vars.

- [ ] **Step 3: Update api/main.py startup and get_conn**

At the top of `api/main.py`, add to the imports block (after existing `from api.db import ...` lines):

```python
import logging
from api import sheets as sheets_module
```

Replace the startup block (currently `config = Config()` / `init_db(config.sqlite_path)`) with:

```python
logger = logging.getLogger(__name__)

config = Config()

# Sheets mode: in-memory SQLite rebuilt from Google Sheets on startup
_sheets_client = None
_mem_conn = None

if config.sheets_enabled():
    import sqlite3 as _sqlite3
    from api.db import init_db as _init_db
    _mem_conn = _sqlite3.connect(":memory:", check_same_thread=False)
    _mem_conn.row_factory = _sqlite3.Row
    _init_db(":memory:")  # create schema on the file path (no-op for :memory: via helper below)

    # init_db only accepts a path string, so initialise schema directly on _mem_conn
    _mem_conn.executescript("""
        CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY);
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY, display_name TEXT, created_at TEXT
        );
        CREATE TABLE IF NOT EXISTS guesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL, set_id TEXT NOT NULL,
            clue_number INTEGER NOT NULL, is_correct INTEGER NOT NULL,
            guessed_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS daily_reveals (
            user_id TEXT NOT NULL, set_id TEXT NOT NULL, reveal_date TEXT NOT NULL,
            PRIMARY KEY (user_id, set_id)
        );
        INSERT OR IGNORE INTO schema_version (version) VALUES (1);
    """)

    try:
        _sheets_client = sheets_module.get_sheets_client(config.google_service_account_json)
        data = sheets_module.load_all(_sheets_client, config.google_sheets_id)
        sheets_module.replay_into_db(_mem_conn, data)
        logger.info("Sheets mode: replayed %d users, %d guesses, %d reveals.",
                    len(data["users"]), len(data["guesses"]), len(data["daily_reveals"]))
    except Exception as e:
        logger.error("Sheets startup failed (%s) — starting with empty in-memory db.", e)
        _sheets_client = None
else:
    init_db(config.sqlite_path)

bank = load_bank(config.bank_path)
```

Replace the existing `get_conn()` function with:

```python
def get_conn() -> sqlite3.Connection:
    """Return the active SQLite connection (in-memory if Sheets mode, file otherwise)."""
    if _mem_conn is not None:
        return _mem_conn
    conn = sqlite3.connect(config.sqlite_path)
    conn.row_factory = sqlite3.Row
    return conn
```

Add a helper at module level (after `get_conn`):

```python
def _close_conn(conn: sqlite3.Connection) -> None:
    """Close conn only if it is not the shared in-memory connection."""
    if conn is not _mem_conn:
        conn.close()
```

Now update all `finally: conn.close()` blocks in the endpoint functions to use `_close_conn(conn)` instead of `conn.close()`. There are four endpoints that do this: `leaderboard`, `score`, `reveal`, `user_status`. Replace each `conn.close()` inside a `finally:` block with `_close_conn(conn)`.

- [ ] **Step 4: Wire Sheets writes into the score and reveal endpoints**

In the `score` endpoint, after `record_guess(...)` and before `points_today = ...`, add:

```python
        if _sheets_client:
            sheets_module.sheets_write_with_retry(
                sheets_module.upsert_user_row,
                _sheets_client, config.google_sheets_id,
                req.user_id, req.display_name,
                sqlite3.connect(":memory:").execute("SELECT datetime('now')").fetchone()[0],
            )
            sheets_module.sheets_write_with_retry(
                sheets_module.append_guess,
                _sheets_client, config.google_sheets_id,
                {
                    "user_id": req.user_id,
                    "set_id": req.set_id,
                    "clue_number": req.clue_number,
                    "is_correct": 1,
                    "guessed_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
                },
            )
```

Wait — that's messy. Instead, add this import at the top of `main.py`:

```python
from datetime import datetime, timezone
```

Then in the `score` endpoint, after `record_guess(conn, req.user_id, req.set_id, req.clue_number, is_correct=True)`, add:

```python
        if _sheets_client:
            _now = datetime.now(timezone.utc).isoformat()
            sheets_module.sheets_write_with_retry(
                sheets_module.upsert_user_row,
                _sheets_client, config.google_sheets_id,
                req.user_id, req.display_name, _now,
            )
            sheets_module.sheets_write_with_retry(
                sheets_module.append_guess,
                _sheets_client, config.google_sheets_id,
                {
                    "user_id": req.user_id,
                    "set_id": req.set_id,
                    "clue_number": req.clue_number,
                    "is_correct": 1,
                    "guessed_at": _now,
                },
            )
```

In the `reveal` endpoint, after `record_reveal(conn, req.user_id, req.set_id, reveal_date)`, add:

```python
        if _sheets_client:
            _now = datetime.now(timezone.utc).isoformat()
            sheets_module.sheets_write_with_retry(
                sheets_module.upsert_user_row,
                _sheets_client, config.google_sheets_id,
                req.user_id, req.display_name, _now,
            )
            sheets_module.sheets_write_with_retry(
                sheets_module.append_reveal,
                _sheets_client, config.google_sheets_id,
                {
                    "user_id": req.user_id,
                    "set_id": req.set_id,
                    "reveal_date": reveal_date,
                },
            )
```

- [ ] **Step 5: Run the new test**

```bash
pytest tests/test_api.py::test_sheets_mode_leaderboard_uses_replayed_data -v
```

Expected: PASS.

- [ ] **Step 6: Run full test suite**

```bash
pytest tests/ -v
```

Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add api/main.py
git commit -m "feat: wire Google Sheets startup replay and write-through into main.py"
```

---

### Task 4: Update render.yaml and push

**Files:**
- Modify: `api/render.yaml`

**Interfaces:**
- Consumes: nothing new
- Produces: Render deployment config that includes the two new env var keys (values set manually in Render dashboard)

- [ ] **Step 1: Add new env var stubs to render.yaml**

Open `api/render.yaml`. It currently ends at `ALLOWED_ORIGINS`. Add two new entries (values left empty — they are set as secrets in the Render dashboard):

```yaml
      - key: GOOGLE_SHEETS_ID
        value: ""
      - key: GOOGLE_SERVICE_ACCOUNT_JSON
        value: ""
```

- [ ] **Step 2: Run full test suite one final time**

```bash
pytest tests/ -v
```

Expected: all tests pass.

- [ ] **Step 3: Commit and push**

```bash
git add api/render.yaml
git commit -m "feat: add GOOGLE_SHEETS_ID and GOOGLE_SERVICE_ACCOUNT_JSON to render.yaml"
git push origin master
```

---

## Post-implementation: Google Cloud setup steps (manual)

After all tasks are complete, the user must:

1. Go to [console.cloud.google.com](https://console.cloud.google.com) → New Project → name it `rockbusters`
2. Enable **Google Sheets API** and **Google Drive API** for the project
3. IAM & Admin → Service Accounts → Create → download JSON key
4. Create a new Google Sheet with three tabs named exactly: `users`, `guesses`, `daily_reveals`
5. Add a header row to each tab:
   - `users`: `user_id | display_name | created_at`
   - `guesses`: `user_id | set_id | clue_number | is_correct | guessed_at`
   - `daily_reveals`: `user_id | set_id | reveal_date`
6. Share the sheet with the service account email (Editor access)
7. In Render dashboard → Environment → set:
   - `GOOGLE_SHEETS_ID` = the sheet ID from its URL
   - `GOOGLE_SERVICE_ACCOUNT_JSON` = the entire JSON key file contents as a single line
8. Trigger a new Render deploy
