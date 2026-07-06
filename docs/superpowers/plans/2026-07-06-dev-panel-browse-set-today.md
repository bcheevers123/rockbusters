# Dev Panel Browse, Random & Set as Today — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a dev-panel Browse modal (with Random + Set as Today), a server-side daily override API, and clean all em dashes from the question bank YAML.

**Architecture:** The backend gains a `daily_override` SQLite table and two new endpoints (`GET /api/bank`, `POST /api/admin/set-today`). `get_todays_set` checks the override table first. The frontend dev panel gains Browse and Random buttons; the Browse modal lets the dev preview or pin any set for today across all users. Em dashes are removed from 42 batch YAML files by a Python script, followed by recompilation of the JSON exports.

**Tech Stack:** Python 3, FastAPI, SQLite, vanilla JS (no bundler), PyYAML, pytest, Claude API for em-dash rewrite (via workflow).

## Global Constraints

- Passcode hash `7cad4eb0e04bd259d1291faa24c9b04a52cb6697ede50931cde44e046019c20d` (SHA-256 of "monkeynews") — never store plaintext.
- `daily_override.valid_date` stored as `YYYY-MM-DD` in `Europe/London` timezone.
- Override auto-expires when local date no longer matches — no cron, no cleanup job.
- Frontend uses no framework, no bundler — plain DOM manipulation only.
- All new backend code follows existing patterns in `api/db.py`, `api/game_service.py`, `api/main.py`.
- Tests use `pytest`; run with `pytest tests/ -v`.
- Bank JSON exports live at `docs/data/rockbusters.json` and `docs/data/rockbusters-answers.json`.
- Em dash cleanup: preserve Karl Pilkington voice, meaning, and phonetic validity of every clue.

---

## File Map

| File | Change |
|------|--------|
| `api/db.py` | Add `daily_override` table to `_create_schema`; add `get_daily_override`, `set_daily_override` |
| `api/game_service.py` | Add optional `conn` param to `get_todays_set`; check override before rotation |
| `api/main.py` | Add `GET /api/bank` and `POST /api/admin/set-today`; pass `conn` to `get_todays_set` in `/api/today` |
| `tests/test_daily_override.py` | New: unit tests for override DB functions and game_service override logic |
| `tests/test_api.py` | Add tests for `GET /api/bank` and `POST /api/admin/set-today` |
| `docs/index.html` | Add Browse modal HTML + Browse/Random buttons to dev panel |
| `docs/app.js` | Add `_bankSets` cache, `devBrowse`, `devRandom`, modal open/close/select/preview/set-today, wire buttons |
| `docs/style.css` | Add `.dev-browse-modal` and related styles |
| `data/batches/batch-*.yaml` (42 files) | Remove em dashes; replace with grammatically correct alternatives |
| `data/rockbusters.yaml` | Regenerated from batches via `scripts/reorder_bank.py` |
| `docs/data/rockbusters.json` | Regenerated via `scripts/export_json.py` |
| `docs/data/rockbusters-answers.json` | Regenerated via `scripts/export_json.py` |

---

## Task 1: DB — daily_override table and helper functions

**Files:**
- Modify: `api/db.py`
- Create: `tests/test_daily_override.py`

**Interfaces:**
- Produces:
  - `get_daily_override(conn: sqlite3.Connection) -> str | None` — returns `set_id` if today's override exists, else `None`. Takes today's date string as a parameter for testability: `get_daily_override(conn, today_str: str) -> str | None`
  - `set_daily_override(conn: sqlite3.Connection, set_id: str, date_str: str) -> None` — replaces current override row

- [ ] **Step 1: Write failing tests**

Create `tests/test_daily_override.py`:

```python
"""Tests for daily_override DB helpers."""

import sqlite3
import pytest
from api.db import _create_schema, get_daily_override, set_daily_override


@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.row_factory = sqlite3.Row
    _create_schema(c)
    yield c
    c.close()


def test_get_daily_override_empty(conn):
    """Returns None when no override row exists."""
    assert get_daily_override(conn, "2026-07-06") is None


def test_set_and_get_daily_override(conn):
    """set then get returns the set_id for matching date."""
    set_daily_override(conn, "sweetbusters-001", "2026-07-06")
    assert get_daily_override(conn, "2026-07-06") == "sweetbusters-001"


def test_override_different_date_returns_none(conn):
    """Override for a different date returns None."""
    set_daily_override(conn, "sweetbusters-001", "2026-07-05")
    assert get_daily_override(conn, "2026-07-06") is None


def test_set_override_replaces_existing(conn):
    """Writing a second override replaces the first."""
    set_daily_override(conn, "sweetbusters-001", "2026-07-06")
    set_daily_override(conn, "filmbusters-002", "2026-07-06")
    assert get_daily_override(conn, "2026-07-06") == "filmbusters-002"
```

- [ ] **Step 2: Run tests to verify they fail**

```
pytest tests/test_daily_override.py -v
```
Expected: ImportError or AttributeError — `get_daily_override` not defined yet.

- [ ] **Step 3: Add `daily_override` table to `_create_schema` in `api/db.py`**

After the `daily_reveals` CREATE TABLE block, add:

```python
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS daily_override (
            set_id     TEXT NOT NULL,
            valid_date TEXT NOT NULL
        )
        """
    )
```

- [ ] **Step 4: Add `get_daily_override` and `set_daily_override` to `api/db.py`**

Add after the existing `get_leaderboard` function:

```python
def get_daily_override(conn: sqlite3.Connection, today_str: str) -> str | None:
    """Return the override set_id if one exists for today_str (YYYY-MM-DD), else None."""
    row = conn.execute(
        "SELECT set_id FROM daily_override WHERE valid_date = ?",
        (today_str,),
    ).fetchone()
    return row[0] if row else None


def set_daily_override(conn: sqlite3.Connection, set_id: str, date_str: str) -> None:
    """Replace any existing override with set_id for date_str."""
    conn.execute("DELETE FROM daily_override")
    conn.execute(
        "INSERT INTO daily_override (set_id, valid_date) VALUES (?, ?)",
        (set_id, date_str),
    )
    conn.commit()
```

- [ ] **Step 5: Update `api/main.py` import of db functions**

In `api/main.py`, add `get_daily_override` and `set_daily_override` to the import from `api.db`:

```python
from api.db import (
    _create_schema,
    get_daily_override,
    get_leaderboard,
    get_user_score_today,
    has_correct_guess,
    has_revealed,
    init_db,
    record_guess,
    record_reveal,
    set_daily_override,
    upsert_user,
)
```

- [ ] **Step 6: Run tests to verify they pass**

```
pytest tests/test_daily_override.py -v
```
Expected: 4 passed.

- [ ] **Step 7: Commit**

```bash
git add api/db.py tests/test_daily_override.py
git commit -m "feat: add daily_override table and db helpers"
```

---

## Task 2: game_service — override check before rotation

**Files:**
- Modify: `api/game_service.py`
- Modify: `tests/test_daily_rotation.py`

**Interfaces:**
- Consumes: `get_daily_override(conn, today_str) -> str | None` from `api/db`
- Produces: `get_todays_set(bank, config, conn=None) -> RockbusterSet` — unchanged signature when `conn=None`; checks override when `conn` is provided

- [ ] **Step 1: Write failing test**

Add to `tests/test_daily_rotation.py`:

```python
import sqlite3
from api.db import _create_schema, set_daily_override
from api.config import Config
from api.game_service import get_todays_set


def test_override_returns_pinned_set(three_set_bank):
    """When a daily override is set, get_todays_set returns the pinned set."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    _create_schema(conn)

    import datetime
    import pytz
    config = Config()
    tz = pytz.timezone(config.timezone)
    today_str = datetime.datetime.now(tz).strftime("%Y-%m-%d")

    set_daily_override(conn, "set-beta", today_str)

    result = get_todays_set(three_set_bank, config, conn=conn)
    assert result.id == "set-beta"
    conn.close()


def test_override_unknown_id_falls_back_to_rotation(three_set_bank):
    """When the override set_id doesn't exist in the bank, fall back to rotation."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    _create_schema(conn)

    import datetime
    import pytz
    config = Config()
    tz = pytz.timezone(config.timezone)
    today_str = datetime.datetime.now(tz).strftime("%Y-%m-%d")

    set_daily_override(conn, "nonexistent-set-999", today_str)

    # Should fall back to rotation without raising
    result = get_todays_set(three_set_bank, config, conn=conn)
    assert result.id in {s.id for s in three_set_bank}
    conn.close()


def test_no_conn_uses_rotation(three_set_bank):
    """With conn=None, get_todays_set uses date rotation as before."""
    config = Config()
    result = get_todays_set(three_set_bank, config, conn=None)
    assert result.id in {s.id for s in three_set_bank}
```

- [ ] **Step 2: Run tests to verify they fail**

```
pytest tests/test_daily_rotation.py::test_override_returns_pinned_set -v
```
Expected: TypeError — `get_todays_set` doesn't accept `conn` yet.

- [ ] **Step 3: Update `api/game_service.py`**

Replace the file content with:

```python
"""Rockbusters game service — daily set selection and state management."""

import datetime
from typing import List, Optional

import pytz

from api.config import Config
from api.content_bank import RockbusterSet, get_enabled_sets
from api.db import get_daily_override

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


def get_todays_set(
    bank: List[RockbusterSet],
    config: Config,
    conn=None,
) -> RockbusterSet:
    """Return today's RockbusterSet.

    If *conn* is provided, checks the daily_override table first. If a valid
    override exists and its set_id is in the enabled bank, returns that set.
    Otherwise falls back to date-based rotation.
    """
    tz = pytz.timezone(config.timezone)
    now_local = datetime.datetime.now(tz)
    today = now_local.date()
    today_str = today.strftime("%Y-%m-%d")

    if conn is not None:
        override_id = get_daily_override(conn, today_str)
        if override_id:
            enabled = get_enabled_sets(bank)
            match = next((s for s in enabled if s.id == override_id), None)
            if match:
                return match

    return get_set_for_date(bank, today)
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/test_daily_rotation.py -v
```
Expected: all existing + 3 new tests pass.

- [ ] **Step 5: Commit**

```bash
git add api/game_service.py tests/test_daily_rotation.py
git commit -m "feat: get_todays_set checks daily_override before rotation"
```

---

## Task 3: API — GET /api/bank and POST /api/admin/set-today, wire override into /api/today

**Files:**
- Modify: `api/main.py`
- Modify: `tests/test_api.py`

**Interfaces:**
- Consumes: `get_daily_override`, `set_daily_override` from `api.db`; `get_todays_set(bank, config, conn)` from `api.game_service`
- Produces:
  - `GET /api/bank` → `[{"id": str, "title": str, "topic": str}]`
  - `POST /api/admin/set-today?set_id=X&secret=Y` → `{"ok": true, "set_id": str}` or 403/404

- [ ] **Step 1: Write failing tests**

Add to `tests/test_api.py` (at the end, before the Sheets-mode tests):

```python
def test_bank_endpoint_returns_list(client):
    """GET /api/bank returns a list of dicts with id, title, topic."""
    resp = client.get("/api/bank")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
    first = data[0]
    assert "id" in first
    assert "title" in first
    assert "topic" in first
    assert "answer" not in first  # no sensitive fields
    assert "clues" not in first


def test_set_today_wrong_passcode_403(client):
    """POST /api/admin/set-today with wrong passcode → 403."""
    resp = client.post("/api/admin/set-today", params={"set_id": "any", "secret": "wrongpassword"})
    assert resp.status_code == 403


def test_set_today_unknown_set_id_404(client):
    """POST /api/admin/set-today with valid passcode but unknown set_id → 404."""
    resp = client.post(
        "/api/admin/set-today",
        params={"set_id": "does-not-exist-999", "secret": "monkeynews"},
    )
    assert resp.status_code == 404


def test_set_today_valid_200(client):
    """POST /api/admin/set-today with valid passcode and real set_id → 200."""
    # Get a real set_id from the bank endpoint
    bank_resp = client.get("/api/bank")
    first_id = bank_resp.json()[0]["id"]

    resp = client.post(
        "/api/admin/set-today",
        params={"set_id": first_id, "secret": "monkeynews"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("ok") is True
    assert body.get("set_id") == first_id


def test_today_respects_override(client):
    """After set-today, GET /api/today returns the overridden set."""
    bank_resp = client.get("/api/bank")
    sets = bank_resp.json()
    # Pick the last set (least likely to be today's natural rotation)
    target_id = sets[-1]["id"]

    client.post(
        "/api/admin/set-today",
        params={"set_id": target_id, "secret": "monkeynews"},
    )

    today_resp = client.get("/api/today")
    assert today_resp.status_code == 200
    assert today_resp.json()["set_id"] == target_id
```

- [ ] **Step 2: Run tests to verify they fail**

```
pytest tests/test_api.py::test_bank_endpoint_returns_list tests/test_api.py::test_set_today_wrong_passcode_403 -v
```
Expected: 404 — endpoints don't exist yet.

- [ ] **Step 3: Add `GET /api/bank` to `api/main.py`**

Add after the `health` endpoint:

```python
@app.get("/api/bank")
def bank_list():
    """Return all enabled sets as a list of {id, title, topic}."""
    from api.content_bank import get_enabled_sets
    enabled = get_enabled_sets(bank)
    return [{"id": s.id, "title": s.title, "topic": s.topic} for s in enabled]
```

- [ ] **Step 4: Add `POST /api/admin/set-today` to `api/main.py`**

Add after `bank_list`:

```python
@app.post("/api/admin/set-today")
def admin_set_today(set_id: str = Query(...), secret: str = Query(...)):
    """Pin set_id as today's set. Expires automatically at midnight (local time)."""
    secret_hash = hashlib.sha256(secret.strip().encode()).hexdigest()
    if secret_hash != _DEV_PASSCODE_HASH:
        raise HTTPException(status_code=403, detail="Forbidden")

    from api.content_bank import get_enabled_sets
    enabled = get_enabled_sets(bank)
    if not any(s.id == set_id for s in enabled):
        raise HTTPException(status_code=404, detail=f"Set '{set_id}' not found in enabled bank.")

    tz = pytz.timezone(config.timezone)
    today_str = datetime.datetime.now(tz).strftime("%Y-%m-%d")

    conn = get_conn()
    try:
        with _mem_lock if _mem_conn is not None else contextlib.nullcontext():
            set_daily_override(conn, set_id, today_str)
    finally:
        _close_conn(conn)

    return {"ok": True, "set_id": set_id}
```

- [ ] **Step 5: Update `/api/today` to pass `conn` into `get_todays_set`**

In `api/main.py`, replace the `today()` function body:

```python
@app.get("/api/today")
def today():
    """Return today's set — clues only, no answers or aliases."""
    conn = get_conn()
    try:
        with _mem_lock if _mem_conn is not None else contextlib.nullcontext():
            todays_set = get_todays_set(bank, config, conn=conn)
    finally:
        _close_conn(conn)

    tz = pytz.timezone(config.timezone)
    local_date = datetime.datetime.now(tz).date()

    return {
        "set_id": todays_set.id,
        "title": todays_set.title,
        "topic": todays_set.topic,
        "intro": todays_set.intro,
        "prize": todays_set.prize,
        "date": format_date_british(local_date),
        "clues": [
            {
                "number": c.number,
                "initials": c.initials,
                "clue": c.clue,
            }
            for c in todays_set.clues
        ],
    }
```

- [ ] **Step 6: Run all tests**

```
pytest tests/ -v
```
Expected: all pass.

- [ ] **Step 7: Commit**

```bash
git add api/main.py tests/test_api.py
git commit -m "feat: GET /api/bank, POST /api/admin/set-today, wire override into /api/today"
```

---

## Task 4: Frontend — Browse modal HTML + CSS

**Files:**
- Modify: `docs/index.html`
- Modify: `docs/style.css`

**Interfaces:**
- Produces: HTML elements with IDs used by Task 5's JS:
  - `#dev-browse-btn` — Browse button in dev panel
  - `#dev-random-btn` — Random button in dev panel
  - `#dev-browse-modal` — modal overlay
  - `#dev-browse-list` — scrollable set list container
  - `#dev-browse-random-btn` — Random button inside modal header
  - `#dev-browse-close-btn` — close button inside modal header
  - `#dev-browse-preview-btn` — Preview button in modal footer
  - `#dev-browse-set-today-btn` — Set as Today button in modal footer

- [ ] **Step 1: Add Browse and Random buttons to dev panel in `docs/index.html`**

Replace the dev panel block:

```html
  <!-- Dev panel — only shown after passcode auth -->
  <div id="dev-panel" class="dev-panel" style="display:none" aria-hidden="true">
    <span class="dev-label">Dev</span>
    <button id="dev-prev-btn" class="dev-btn">&#8592; Prev</button>
    <span id="dev-set-info" class="dev-set-info"></span>
    <button id="dev-next-btn" class="dev-btn">Next &#8594;</button>
    <button id="dev-browse-btn" class="dev-btn">Browse</button>
    <button id="dev-random-btn" class="dev-btn">Random</button>
    <button id="dev-reset-btn" class="dev-btn">Today</button>
    <button id="dev-reset-lb-btn" class="dev-btn dev-btn-danger">Reset LB</button>
    <button id="dev-lock-btn" class="dev-btn dev-btn-danger">Lock</button>
  </div>

  <!-- Browse modal — only shown when dev panel is unlocked -->
  <div id="dev-browse-modal" class="dev-browse-modal" style="display:none" aria-hidden="true">
    <div class="dev-browse-dialog">
      <div class="dev-browse-header">
        <span class="dev-browse-title">Browse Sets</span>
        <button id="dev-browse-random-btn" class="dev-btn">Random</button>
        <button id="dev-browse-close-btn" class="dev-btn">&#10005;</button>
      </div>
      <div id="dev-browse-list" class="dev-browse-list"></div>
      <div class="dev-browse-footer">
        <button id="dev-browse-preview-btn" class="dev-btn" disabled>Preview</button>
        <button id="dev-browse-set-today-btn" class="dev-btn dev-btn-danger" disabled>Set as Today</button>
      </div>
    </div>
  </div>
```

- [ ] **Step 2: Add modal styles to `docs/style.css`**

Add after the `.dev-set-info` block (after line 840):

```css
/* ---------------------------------------------------------------------------
   Dev browse modal
--------------------------------------------------------------------------- */

.dev-browse-modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  z-index: 600;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dev-browse-dialog {
  background: #1a1a2e;
  border: 2px solid #e94560;
  border-radius: 8px;
  width: min(600px, 92vw);
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.dev-browse-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #333;
  flex-shrink: 0;
}

.dev-browse-title {
  flex: 1;
  font-weight: 700;
  font-size: 0.9rem;
  color: #e94560;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.dev-browse-list {
  flex: 1;
  overflow-y: auto;
  padding: 0.5rem 0;
}

.dev-browse-group-label {
  padding: 0.4rem 1rem 0.2rem;
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #888;
}

.dev-browse-row {
  padding: 0.45rem 1rem;
  cursor: pointer;
  display: flex;
  gap: 0.75rem;
  align-items: baseline;
  transition: background 0.1s;
}

.dev-browse-row:hover {
  background: #16213e;
}

.dev-browse-row.selected {
  background: #0f3460;
  color: #fff;
}

.dev-browse-row-id {
  font-size: 0.72rem;
  color: #888;
  flex-shrink: 0;
  font-family: monospace;
}

.dev-browse-row.selected .dev-browse-row-id {
  color: #aac;
}

.dev-browse-row-title {
  font-size: 0.82rem;
  color: #ddd;
}

.dev-browse-footer {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
  padding: 0.75rem 1rem;
  border-top: 1px solid #333;
  flex-shrink: 0;
}
```

- [ ] **Step 3: Verify HTML is valid**

Open `docs/index.html` in a browser and confirm the page loads without errors (the modal is hidden by default).

- [ ] **Step 4: Commit**

```bash
git add docs/index.html docs/style.css
git commit -m "feat: Browse modal HTML and CSS, Browse/Random buttons in dev panel"
```

---

## Task 5: Frontend — Browse modal JS logic

**Files:**
- Modify: `docs/app.js`

**Interfaces:**
- Consumes: `getApiUrl()`, `devSetOffset()`, `devGetOffset()`, `devIsUnlocked()`, `loadQuiz()`, `devUpdateInfo()` — all existing module-level functions in `app.js`
- Consumes: HTML element IDs from Task 4
- Produces: `devBrowse()`, `devRandom()` — exposed on `window`; wired to buttons in `wireQuizButtons()`

- [ ] **Step 1: Add `_bankSets` cache and bank-fetch helper after the dev globals**

In `app.js`, after `const DEV_OFFSET_KEY = 'rockbusters_dev_offset';`, add:

```javascript
// ---------------------------------------------------------------------------
// Dev browse modal state
// ---------------------------------------------------------------------------
let _bankSets = null;
let _browseSelectedId = null;

async function fetchBankSets() {
  if (_bankSets) return _bankSets;
  const apiUrl = getApiUrl();
  if (!apiUrl) return [];
  const res = await fetch(`${apiUrl}/api/bank`);
  if (!res.ok) return [];
  _bankSets = await res.json();
  return _bankSets;
}
```

- [ ] **Step 2: Add `devBrowse` function**

Add after `devResetLeaderboard()`:

```javascript
async function devBrowse() {
  const modal = document.getElementById('dev-browse-modal');
  if (!modal) return;

  const sets = await fetchBankSets();
  if (!sets.length) { window.alert('No API URL configured or bank unavailable.'); return; }

  // Build grouped list
  const listEl = document.getElementById('dev-browse-list');
  listEl.innerHTML = '';
  _browseSelectedId = null;

  // Group by topic
  const groups = {};
  sets.forEach(s => {
    if (!groups[s.topic]) groups[s.topic] = [];
    groups[s.topic].push(s);
  });

  Object.entries(groups).forEach(([topic, items]) => {
    const label = document.createElement('div');
    label.className = 'dev-browse-group-label';
    label.textContent = topic;
    listEl.appendChild(label);

    items.forEach(s => {
      const row = document.createElement('div');
      row.className = 'dev-browse-row';
      row.dataset.setId = s.id;

      const idSpan = document.createElement('span');
      idSpan.className = 'dev-browse-row-id';
      idSpan.textContent = s.id;

      const titleSpan = document.createElement('span');
      titleSpan.className = 'dev-browse-row-title';
      titleSpan.textContent = s.title;

      row.appendChild(idSpan);
      row.appendChild(titleSpan);
      row.addEventListener('click', () => browseSelectRow(row, s.id));
      listEl.appendChild(row);
    });
  });

  // Reset footer buttons
  const previewBtn = document.getElementById('dev-browse-preview-btn');
  const setTodayBtn = document.getElementById('dev-browse-set-today-btn');
  if (previewBtn) previewBtn.disabled = true;
  if (setTodayBtn) setTodayBtn.disabled = true;

  modal.style.display = 'flex';
  modal.removeAttribute('aria-hidden');
}

function browseSelectRow(row, setId) {
  // Deselect previous
  const listEl = document.getElementById('dev-browse-list');
  listEl.querySelectorAll('.dev-browse-row.selected').forEach(r => r.classList.remove('selected'));
  row.classList.add('selected');
  _browseSelectedId = setId;

  const previewBtn = document.getElementById('dev-browse-preview-btn');
  const setTodayBtn = document.getElementById('dev-browse-set-today-btn');
  if (previewBtn) previewBtn.disabled = false;
  if (setTodayBtn) setTodayBtn.disabled = false;
}

function browseSelectRandom() {
  if (!_bankSets || !_bankSets.length) return;
  const randomSet = _bankSets[Math.floor(Math.random() * _bankSets.length)];
  const listEl = document.getElementById('dev-browse-list');
  const row = listEl.querySelector(`[data-set-id="${randomSet.id}"]`);
  if (row) {
    row.scrollIntoView({ block: 'center' });
    browseSelectRow(row, randomSet.id);
  }
}

function browseClose() {
  const modal = document.getElementById('dev-browse-modal');
  if (modal) { modal.style.display = 'none'; modal.setAttribute('aria-hidden', 'true'); }
}

async function browsePreview() {
  if (!_browseSelectedId || !_bankSets) return;
  // Find the index of this set in the enabled list (same order as rotation)
  const idx = _bankSets.findIndex(s => s.id === _browseSelectedId);
  if (idx === -1) return;

  // Calculate offset: we want getTodaysIndex(total) === idx
  // getTodaysIndex = (diffDays + offset) % total
  // offset = idx - diffDays (mod total)
  const total = _bankSets.length;
  const today = getTodayLondon();
  const EPOCH_DATE = new Date(Date.UTC(2026, 0, 2));
  const diffDays = Math.floor((today.getTime() - EPOCH_DATE.getTime()) / (1000 * 60 * 60 * 24));
  const offset = (((idx - diffDays) % total) + total) % total;

  devSetOffset(offset);
  browseClose();
  await loadQuiz();
}

async function browseSetToday() {
  if (!_browseSelectedId) return;
  const secret = window.prompt('Dev passcode:');
  if (!secret) return;
  const apiUrl = getApiUrl();
  if (!apiUrl) { window.alert('No API URL configured.'); return; }
  try {
    const res = await fetch(
      `${apiUrl}/api/admin/set-today?set_id=${encodeURIComponent(_browseSelectedId)}&secret=${encodeURIComponent(secret)}`,
      { method: 'POST' }
    );
    const data = await res.json();
    if (res.ok) {
      browseClose();
      await loadQuiz();
    } else {
      window.alert(`Error: ${data.detail || res.status}`);
    }
  } catch (e) {
    window.alert(`Failed: ${e.message}`);
  }
}
```

- [ ] **Step 3: Add `devRandom` function**

Add after `browseSetToday()`:

```javascript
async function devRandom() {
  const sets = await fetchBankSets();
  if (!sets.length) { window.alert('No API URL configured or bank unavailable.'); return; }
  const randomSet = sets[Math.floor(Math.random() * sets.length)];
  const total = sets.length;
  const today = getTodayLondon();
  const EPOCH_DATE = new Date(Date.UTC(2026, 0, 2));
  const diffDays = Math.floor((today.getTime() - EPOCH_DATE.getTime()) / (1000 * 60 * 60 * 24));
  const idx = sets.findIndex(s => s.id === randomSet.id);
  const offset = (((idx - diffDays) % total) + total) % total;
  devSetOffset(offset);
  await loadQuiz();
}
```

- [ ] **Step 4: Wire new buttons in `wireQuizButtons()`**

In `wireQuizButtons()`, add after the existing dev panel button wiring:

```javascript
  const devBrowseBtn = document.getElementById('dev-browse-btn');
  const devRandomBtn = document.getElementById('dev-random-btn');
  const devBrowseRandomBtn = document.getElementById('dev-browse-random-btn');
  const devBrowseCloseBtn = document.getElementById('dev-browse-close-btn');
  const devBrowsePreviewBtn = document.getElementById('dev-browse-preview-btn');
  const devBrowseSetTodayBtn = document.getElementById('dev-browse-set-today-btn');
  const devBrowseModal = document.getElementById('dev-browse-modal');

  if (devBrowseBtn)       devBrowseBtn.addEventListener('click', devBrowse);
  if (devRandomBtn)       devRandomBtn.addEventListener('click', devRandom);
  if (devBrowseRandomBtn) devBrowseRandomBtn.addEventListener('click', browseSelectRandom);
  if (devBrowseCloseBtn)  devBrowseCloseBtn.addEventListener('click', browseClose);
  if (devBrowsePreviewBtn) devBrowsePreviewBtn.addEventListener('click', browsePreview);
  if (devBrowseSetTodayBtn) devBrowseSetTodayBtn.addEventListener('click', browseSetToday);
  if (devBrowseModal) devBrowseModal.addEventListener('click', e => { if (e.target === devBrowseModal) browseClose(); });
```

Also add `Escape` key close support in the existing `document.addEventListener('keydown', ...)` handler — update it to:

```javascript
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      closeHelp();
      browseClose();
    }
  });
```

- [ ] **Step 5: Expose new functions on `window`**

Add to the window exposure block at the bottom of `app.js`:

```javascript
window.devBrowse = devBrowse;
window.devRandom = devRandom;
```

- [ ] **Step 6: Commit**

```bash
git add docs/app.js
git commit -m "feat: dev panel Browse modal and Random button JS"
```

---

## Task 6: Em dash cleanup — batch YAML files

**Files:**
- Modify: `data/batches/batch-003.yaml`, `batch-004.yaml`, `batch-005.yaml`, `batch-011.yaml`, `batch-018.yaml`, `batch-028.yaml`, `batch-037.yaml`, `batch-038.yaml`, `batch-039.yaml`, `batch-040.yaml`, `batch-041.yaml`, `batch-042.yaml`, `batch-043.yaml`, `batch-044.yaml`, `batch-046.yaml`, `batch-057.yaml`, `batch-058.yaml`, `batch-059.yaml`, `batch-060.yaml`, `batch-061.yaml`, `batch-062.yaml`, `batch-063.yaml`, `batch-064.yaml`, `batch-065.yaml`, `batch-066.yaml`, `batch-067.yaml`, `batch-068.yaml`, `batch-069.yaml`, `batch-070.yaml`, `batch-071.yaml`, `batch-072.yaml`, `batch-073.yaml`, `batch-074.yaml`, `batch-075.yaml`, `batch-076.yaml`, `batch-077.yaml`, `batch-078.yaml`, `batch-079.yaml`, `batch-081.yaml`, `batch-082.yaml`, `batch-084.yaml`, `batch-086.yaml`, `batch-087.yaml`, `batch-088.yaml`, `batch-089.yaml`, `batch-091.yaml` (42 files total)
- Modify: `data/rockbusters.yaml` (regenerated)
- Modify: `docs/data/rockbusters.json` (regenerated)
- Modify: `docs/data/rockbusters-answers.json` (regenerated)

**Rules for em dash replacement (preserve Karl Pilkington voice):**

| Pattern | Replacement |
|---------|-------------|
| ` — X — ` (parenthetical) | `, X,` |
| `X — Y` mid-sentence (clause break, both sides are clauses) | `X. Y` (capitalise Y) or `X, Y` if Y continues the thought without a new subject |
| `X — ` trailing pause/afterthought intro | `X. ` or `X: ` |
| ` — that's all` / ` — go on` / ` — have a go` (trailing tag) | `. That's all.` / `. Go on.` etc. |

**Always verify:** the clue still sounds like the answer when read aloud, and the Karl Pilkington register (flat, deadpan, slightly bewildered) is preserved.

- [ ] **Step 1: Process em-dash files using an AI agent**

This task is handled by the `generate-rockbusters` workflow or a dedicated agent pass. For each of the 42 affected batch files:

1. Read the file.
2. For every line containing `—`, rewrite the containing string using the replacement rules above.
3. Write the file back. Do not change any other content.

Run the cleanup as a subagent (see `superpowers:dispatching-parallel-agents` for parallelising across files).

- [ ] **Step 2: Verify no YAML breaks after cleanup**

```
python -c "
import yaml, glob, sys
errors = []
for path in glob.glob('data/batches/batch-*.yaml'):
    try:
        yaml.safe_load(open(path, encoding='utf-8'))
    except Exception as e:
        errors.append(f'{path}: {e}')
if errors:
    for e in errors: print(e)
    sys.exit(1)
else:
    print('All batch files parse OK.')
"
```
Expected: `All batch files parse OK.`

- [ ] **Step 3: Verify no em dashes remain in batch files**

```
python -c "
import glob, sys
found = []
for path in glob.glob('data/batches/batch-*.yaml'):
    text = open(path, encoding='utf-8').read()
    if '—' in text:
        count = text.count('—')
        found.append(f'{path}: {count} em dashes remain')
if found:
    for f in found: print(f)
    sys.exit(1)
else:
    print('No em dashes found in batch files.')
"
```
Expected: `No em dashes found in batch files.`

- [ ] **Step 4: Rebuild `data/rockbusters.yaml` from batches**

The main YAML is NOT built by concatenating batches directly — it is maintained separately and the batches are the source. Update the main YAML by loading all batch files and writing them (preserving order from existing rockbusters.yaml by matching IDs, appending any new ones):

```python
# Run from project root
python -c "
import yaml, glob
from pathlib import Path

batch_dir = Path('data/batches')
all_sets = {}
for path in sorted(batch_dir.glob('batch-*.yaml')):
    sets = yaml.safe_load(open(path, encoding='utf-8'))
    for s in sets:
        all_sets[s['id']] = s

# Load existing order
existing = yaml.safe_load(open('data/rockbusters.yaml', encoding='utf-8'))
existing_ids = [s['id'] for s in existing]

# Replace content with cleaned batch content (keeping order)
updated = []
for sid in existing_ids:
    if sid in all_sets:
        updated.append(all_sets[sid])

# Any IDs in batches not in existing go at the end (shouldn't happen but safe)
for sid, s in all_sets.items():
    if sid not in existing_ids:
        updated.append(s)

with open('data/rockbusters.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(updated, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
print(f'Written {len(updated)} sets to data/rockbusters.yaml')
"
```

- [ ] **Step 5: Validate the compiled bank loads cleanly**

```
python -c "from api.content_bank import load_bank; b = load_bank('data/rockbusters.yaml'); print(f'Loaded {len(b)} sets OK.')"
```
Expected: `Loaded N sets OK.` (no errors).

- [ ] **Step 6: Regenerate JSON exports**

```
python scripts/export_json.py
```
Expected: `Exported N sets to docs/data/rockbusters.json and docs/data/rockbusters-answers.json`

- [ ] **Step 7: Verify no em dashes in exported JSON**

```
python -c "
import json, sys
q = json.load(open('docs/data/rockbusters.json', encoding='utf-8'))
a = json.load(open('docs/data/rockbusters-answers.json', encoding='utf-8'))
found = []
for s in q:
    for clue in s.get('clues', []):
        if '—' in clue.get('clue', ''):
            found.append(f'{s[\"id\"]} clue {clue[\"number\"]}: em dash in question JSON')
    if '—' in s.get('intro', ''):
        found.append(f'{s[\"id\"]}: em dash in intro')
for s in a:
    for clue in s.get('clues', []):
        if '—' in clue.get('reasoning', ''):
            found.append(f'{s[\"id\"]} clue {clue[\"number\"]}: em dash in reasoning')
if found:
    for f in found: print(f)
    sys.exit(1)
else:
    print('No em dashes in exported JSON.')
"
```
Expected: `No em dashes in exported JSON.`

- [ ] **Step 8: Run full test suite**

```
pytest tests/ -v
```
Expected: all pass.

- [ ] **Step 9: Commit**

```bash
git add data/batches/ data/rockbusters.yaml docs/data/rockbusters.json docs/data/rockbusters-answers.json
git commit -m "fix: remove em dashes from all batch YAML files and regenerate exports"
```

---

## Self-Review

**Spec coverage check:**

| Spec requirement | Task |
|-----------------|------|
| `daily_override` table with `set_id`, `valid_date` | Task 1 |
| `get_daily_override(conn, today_str)` | Task 1 |
| `set_daily_override(conn, set_id, date_str)` | Task 1 |
| `get_todays_set` checks override before rotation | Task 2 |
| `GET /api/bank` returns enabled sets | Task 3 |
| `POST /api/admin/set-today` passcode-gated | Task 3 |
| 403 on bad passcode, 404 on unknown set_id | Task 3 |
| `/api/today` respects override | Task 3 |
| Browse + Random buttons in dev panel bar | Task 4 |
| Browse modal with grouped list, Random, close | Task 4 + 5 |
| Preview flow (offset calculation, no passcode) | Task 5 |
| Set as Today flow (prompt, POST, reload) | Task 5 |
| `_bankSets` cache | Task 5 |
| Escape key closes modal | Task 5 |
| Em dashes removed from 42 batch files | Task 6 |
| Rewrite preserves Karl Pilkington voice | Task 6 |
| Validated no YAML breaks | Task 6 |
| `data/rockbusters.yaml` regenerated | Task 6 |
| JSON exports regenerated | Task 6 |

All spec requirements covered. No placeholders remain.
