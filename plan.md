# Rockbusters Web App: Implementation Plan

## Architecture

- **Frontend**: Static HTML/CSS/JS in `/docs` folder → served by GitHub Pages
- **Backend**: Python FastAPI + SQLite in `/api` folder → deployed to Render free tier
- **Content bank**: `data/rockbusters.yaml` (source of truth) + `docs/data/rockbusters.json` (generated for frontend)

Frontend handles: daily rotation, answer display, answer checking (client-side normalization).
Backend handles: recording scores, reveal lockout, leaderboard.

User identity: UUID generated in browser, stored in localStorage alongside display name.

## Global Constraints

- Python 3.11+, FastAPI, SQLite, PyYAML, python-dotenv, pytest
- JavaScript (vanilla, no framework) for frontend
- No LLM calls at runtime, no OpenAI/Anthropic API calls
- No em dashes in answer reasoning output
- Do not bold the prize line
- Do not reference Karl, XFM, Ricky, Steve, or any source inspiration in UI output
- Do not use the exact answer word in a clue where avoidable
- office_safe must be true for all content bank entries
- Timezone default: Europe/London for daily rotation (configurable)
- Answer matching: normalize (lowercase, strip, collapse spaces, remove [^a-z0-9 ]) then compare aliases
- Aliases must include the normalized canonical answer
- YAML is source of truth; JSON is generated for frontend consumption
- Project root: C:\Users\BarryCheevers\OneDrive - Anomali\Desktop\Fun\RockbustersSlack

## Project Structure

```
rockbusters/
  api/
    main.py           ← FastAPI app
    config.py         ← env var config
    db.py             ← SQLite functions
    content_bank.py   ← load/validate YAML
    game_service.py   ← daily rotation
    scoring.py        ← normalize + check_answer
    requirements.txt
    render.yaml       ← Render deployment config
  data/
    rockbusters.yaml  ← source of truth content bank
  docs/               ← GitHub Pages root
    index.html
    app.js
    style.css
    data/
      rockbusters.json  ← generated from YAML
  scripts/
    export_json.py    ← converts YAML → JSON
    dry_run.py        ← smoke test without server
  tests/
    test_normalization.py
    test_content_bank.py
    test_daily_rotation.py
    test_scoring.py
  .env.example
  .gitignore
  README.md
```

## Tasks

---

### Task 1: Project scaffold and dependencies

**Goal**
Create the full directory structure, Python dependency files, config module, database init, `.env.example`, `.gitignore`, and stub files so every subsequent task has a stable foundation.

**Context**
The working directory is `C:\Users\BarryCheevers\OneDrive - Anomali\Desktop\Fun\RockbustersSlack`. A git repo already exists with one empty commit. Previous plan was Slack-based; this is a full pivot to web app + API.

**Relevant files / references**
- Project structure above
- Environment variables: `SQLITE_PATH` (default `rockbusters.db`), `ROCKBUSTERS_BANK_PATH` (default `data/rockbusters.yaml`), `APP_TIMEZONE` (default `Europe/London`), `ALLOWED_ORIGINS` (default `*` for dev, restrict in prod), `API_SECRET` (optional simple token for future use)

**Proposed approach**
1. Create all directories: `api/`, `data/`, `docs/`, `docs/data/`, `scripts/`, `tests/`.
2. Create `api/__init__.py`, `tests/__init__.py`.
3. Write `api/requirements.txt`: `fastapi>=0.111`, `uvicorn[standard]>=0.29`, `python-dotenv>=1.0`, `pyyaml>=6.0`, `pytz>=2024.1`, `pytest>=8.0`, `httpx>=0.27` (for FastAPI test client).
4. Write `api/config.py` — reads env vars, exposes `Config` dataclass with `sqlite_path`, `bank_path`, `timezone`, `allowed_origins`.
5. Write `api/db.py` — `init_db(db_path: str)` creates tables with `CREATE TABLE IF NOT EXISTS`. Schema:
   ```sql
   users(user_id TEXT PRIMARY KEY, display_name TEXT, created_at TEXT)
   guesses(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT, set_id TEXT, clue_number INTEGER, is_correct INTEGER, guessed_at TEXT)
   daily_reveals(user_id TEXT, set_id TEXT, reveal_date TEXT, PRIMARY KEY(user_id, set_id))
   ```
6. Write `.env.example` with all five vars and placeholder values.
7. Write `.gitignore` excluding `.env`, `*.db`, `__pycache__`, `.pytest_cache`, `*.pyc`, `.venv`, `node_modules`.
8. Write empty stub files: `api/main.py`, `api/content_bank.py`, `api/game_service.py`, `api/scoring.py`.
9. Write empty `docs/index.html`, `docs/app.js`, `docs/style.css`.
10. Write `docs/data/.gitkeep`.
11. Write `data/.gitkeep`.
12. Write `scripts/export_json.py` stub and `scripts/dry_run.py` stub.

**Acceptance criteria**
- All directories and files listed in project structure exist.
- `python -c "from api.config import Config; print(Config().timezone)"` prints `Europe/London`.
- `python -c "from api.db import init_db; init_db(':memory:')"` runs without error.
- `.env.example` has all five variable names.
- `.gitignore` excludes `.env` and `*.db`.
- `pip install -r api/requirements.txt` succeeds.

**Verify**
```bash
pip install -r api/requirements.txt
python -c "from api.config import Config; print(Config().timezone)"
python -c "from api.db import init_db; init_db(':memory:')"
```

---

### Task 2: Content bank — YAML + JSON export

**Goal**
Write `api/content_bank.py` with load/validate logic, create `data/rockbusters.yaml` with 3 complete example Rockbuster sets, and write `scripts/export_json.py` that converts the YAML to `docs/data/rockbusters.json`.

**Context**
The YAML is the source of truth maintained by humans. The JSON is consumed by the frontend JS. Both must have identical content. The export script is run manually whenever the YAML is updated.

**Relevant files / references**
- `api/config.py` — `Config` (Task 1)
- YAML schema: `id`, `enabled`, `title`, `topic`, `difficulty`, `office_safe`, `region_relevance`, `intro`, `prize`, `clues[].number`, `clues[].initials`, `clues[].clue`, `clues[].answer`, `clues[].aliases`, `clues[].reasoning`
- Validation: id unique, title/topic/prize required, `office_safe: true`, exactly 3 clues numbered 1–3, initials/clue/answer/reasoning required per clue, `enabled` is boolean.
- Auto-add: if normalized canonical answer not in aliases, add it automatically.
- Normalization: lowercase, strip, collapse spaces, remove `[^a-z0-9 ]`

**3 example Rockbuster sets to create:**

Set 1: sweetbusters-001 — UK sweets
- Clue 1 (W G): Wine Gums — "Right, that bit in your mouth where the teeth sort of live, it's been on the red and white booze. What's happened there?"
- Clue 2 (J B): Jelly Babies — "Little newborns, right, but they're all wobbly. You wouldn't put one in a pram."
- Clue 3 (L H): Love Hearts — "The organ that pumps blood has gone all romantic and that. Bit soppy."
- Prize: "Email in. Winner gets The Best of The Corrs on MiniDisc."
- intro: "Right, Sweetbusters. Rockbusters, but UK sweets again."

Set 2: citybusters-001 — European cities (Paris, Rome, Berlin or similar phonetic-friendly cities)
- Create 3 phonetic clues in the style guide. Do NOT use the city name in the clue.
- Silly, workplace-safe. Early-2000s prize.

Set 3: filmbusters-001 — Famous films (choose 3 with good phonetic potential e.g. Grease, Jaws, Heat, Troy, or similar)
- Create 3 phonetic clues. Do NOT use the film title in the clue.
- Silly, workplace-safe. Early-2000s prize.

**Style guide (apply to all clues):**
- Solvable through phonetic or cryptic wordplay, not a straight definition
- Do not use the answer word directly in the clue
- Tone: silly bloke explaining a bad cryptic clue
- Use sparingly: "Right...", "What's going on there?", "Bit weird.", "What's happened?"
- Safe for work, suitable for UK and US employees

**JSON export (`scripts/export_json.py`):**
- Load YAML via `api.content_bank.load_bank()`
- Export only `enabled: true` sets
- Strip `answer`, `aliases` fields from clues (frontend should not have answers in initial load — they are revealed only when user clicks reveal)
- Include all other fields
- Write to `docs/data/rockbusters.json`
- Print how many sets exported

**Acceptance criteria**
- `load_bank("data/rockbusters.yaml")` returns 3 `RockbusterSet` objects.
- `ContentBankError` raised for missing `prize`, `office_safe: false`, duplicate `id`.
- `normalize("  Wine Gums!! ")` returns `"wine gums"`.
- `python scripts/export_json.py` writes `docs/data/rockbusters.json` with 3 sets, no `answer`/`aliases` fields in clues.
- All 3 sets have phonetic clues that do not use the answer word directly.

**Verify**
```bash
python -c "from api.content_bank import load_bank; s = load_bank('data/rockbusters.yaml'); print(len(s), s[0].title)"
python scripts/export_json.py
cat docs/data/rockbusters.json | python -c "import json,sys; d=json.load(sys.stdin); print(len(d), 'sets')"
```

---

### Task 3: Python API — FastAPI backend

**Goal**
Write `api/main.py` with all API endpoints needed for shared leaderboard, scoring, and reveal lockout. Also complete `api/db.py` with all read/write functions.

**Context**
Frontend does answer checking client-side. API only needs to record scores and reveals. User identity is a UUID + display name from the browser.

**Relevant files / references**
- `api/db.py` — `init_db()` stub (Task 1)
- `api/config.py` — `Config` (Task 1)
- `api/scoring.py` — `normalize()` (Task 4, write stub for now or implement here)

**Complete `api/db.py` with these functions (all accept `conn: sqlite3.Connection`):**
- `upsert_user(conn, user_id: str, display_name: str) -> None`
- `has_revealed(conn, user_id: str, set_id: str) -> bool`
- `record_reveal(conn, user_id: str, set_id: str, reveal_date: str) -> None`
- `has_correct_guess(conn, user_id: str, set_id: str, clue_number: int) -> bool`
- `record_guess(conn, user_id: str, set_id: str, clue_number: int, is_correct: bool) -> None`
- `get_user_score_today(conn, user_id: str, set_id: str) -> int`
- `get_leaderboard(conn, limit: int = 10) -> list[dict]` → `[{user_id, display_name, total_points}]` sorted desc

**API endpoints (`api/main.py`):**

```
GET  /api/health
     → {"status": "ok"}

GET  /api/leaderboard
     → {"leaderboard": [{rank, display_name, total_points, today_points}], "set_id": str}
     today_points: points for the current day's set_id

POST /api/score
     body: {user_id: str, display_name: str, set_id: str, clue_number: int}
     → Records a correct answer for a user.
     → 400 if user has revealed (has_revealed check)
     → 409 if already scored this clue (has_correct_guess check)
     → 200 {"ok": true, "points_today": int}

POST /api/reveal
     body: {user_id: str, display_name: str, set_id: str}
     → Records that user revealed answers. Idempotent (reveal twice = OK).
     → 200 {"ok": true}

GET  /api/user-status?user_id=X&set_id=Y
     → {revealed: bool, correct_clues: [1, 3], points_today: int}

GET  /api/today
     → Today's Rockbuster set (clues only, NO answers or aliases).
     → Intended for external integrations (future Slack bot, Discord bot, etc.)
     → Response shape:
        {
          set_id: str,
          title: str,
          topic: str,
          intro: str,
          prize: str,
          date: str,        ← "1 July 2026"
          clues: [
            {number: int, initials: str, clue: str}
          ]
        }
     → 200 always (uses same daily rotation logic as the frontend)
```

CORS: allow `ALLOWED_ORIGINS` from config. Default `*` for dev.
Startup: call `init_db(config.sqlite_path)`.
Connection: create a new `sqlite3.connect()` per request (simple and safe for SQLite at this scale).

**Acceptance criteria**
- `uvicorn api.main:app --reload` starts without error when `.env` is set.
- `GET /api/health` returns 200 `{"status": "ok"}`.
- `POST /api/score` returns 400 after `POST /api/reveal` for same user+set.
- `POST /api/score` returns 409 on duplicate clue+user+set.
- `GET /api/leaderboard` returns `{"leaderboard": [], "set_id": ...}` when empty.
- All endpoints tested with `httpx` TestClient in `tests/test_api.py`.

**Verify**
```bash
uvicorn api.main:app --reload
curl http://localhost:8000/api/health
```

---

### Task 4: Answer normalisation and matching (Python)

**Goal**
Write `api/scoring.py` with `normalize()` and `check_answer()`. These are used by tests and optionally for server-side validation.

**Context**
Same logic is reimplemented in JavaScript for the frontend (Task 5). Python version used for tests and potential future server-side validation.

**Relevant files / references**
- `api/content_bank.py` — `Clue` dataclass with `.answer`, `.aliases` (Task 2)

**Functions:**
- `normalize(text: str) -> str` — lowercase, strip, collapse spaces, remove `[^a-z0-9 ]`
- `check_answer(clue: Clue, user_input: str) -> bool` — normalize input, compare against all normalized aliases; return False for empty input without raising

**Acceptance criteria**
- `check_answer(wine_gums_clue, "wine gums")` → True
- `check_answer(wine_gums_clue, "  Wine Gums!! ")` → True
- `check_answer(wine_gums_clue, "winegums")` → True (alias)
- `check_answer(wine_gums_clue, "polo mints")` → False
- `check_answer(wine_gums_clue, "")` → False without raising

---

### Task 5: Daily rotation logic (Python + JavaScript)

**Goal**
Write `api/game_service.py` with Python daily rotation, and implement the matching JavaScript daily rotation + answer checking logic in `docs/app.js`.

**Context**
Both frontend and backend must compute the same set for a given date using the same algorithm. The frontend computes it to display the quiz. The backend uses it to validate `set_id` in API calls.

**Relevant files / references**
- `api/content_bank.py` — `get_enabled_sets()` (Task 2)
- `api/config.py` — `Config.timezone` (Task 1)
- `docs/data/rockbusters.json` — frontend loads this

**Python (`api/game_service.py`):**
- `EPOCH = datetime.date(2026, 1, 1)` — fixed, documented
- `get_set_for_date(bank: list, date: date) -> RockbusterSet` — pure, `(date - EPOCH).days % len(enabled)` 
- `get_todays_set(bank: list, config: Config) -> RockbusterSet` — converts UTC to configured TZ, calls above
- Raise `ValueError` if no enabled sets

**JavaScript (`docs/app.js`) — implement full frontend logic:**

Constants:
```js
const EPOCH = new Date('2026-01-01T00:00:00Z');
const TIMEZONE = 'Europe/London';
```

Functions:
- `normalize(text)` — same rules as Python: lowercase, trim, collapse spaces, remove non-alphanumeric-space
- `getTodaysIndex(totalSets)` — compute London date, days since epoch, modulo
- `checkAnswer(clue, userInput)` — normalize input, compare against `clue.aliases`
- `getUserId()` — get or create UUID in localStorage
- `getDisplayName()` / `setDisplayName(name)` — localStorage
- `loadProgress()` / `saveProgress(data)` — localStorage, keyed by set_id + date

**Full UI flow (also in app.js):**
1. Fetch `data/rockbusters.json` on page load
2. Compute today's set index, get today's set
3. Show the quiz (title, date, 3 clues with initials)
4. For each clue: show guess input, check answer, show correct/incorrect feedback
5. Show "Reveal Answers" button — on click: fetch full answers from... wait, answers are NOT in the JSON. So: either (a) fetch from API, or (b) load a separate answers JSON.

**Decision:** Load a second file `docs/data/rockbusters-answers.json` that contains answers and reasoning. The main JSON has no answers. Frontend loads answers only when user clicks Reveal. This avoids an API call for reveals in the trivial case while still protecting answers from casual inspection of the page source (they load on demand). The API `/api/reveal` is still called to record the reveal for leaderboard purposes.

**Generate `docs/data/rockbusters-answers.json` in `scripts/export_json.py`** — same sets but with only `id`, `clues[].number`, `clues[].answer`, `clues[].aliases`, `clues[].reasoning`.

**Acceptance criteria (Python):**
- `get_set_for_date(bank, date(2026,1,1))` same every call
- Different result for `date(2026,1,2)` with 3-set bank
- Cycles, raises ValueError on empty bank

**Acceptance criteria (JS):**
- `normalize("  Wine Gums!! ")` returns `"wine gums"`
- `checkAnswer({aliases:["wine gums","winegums"]}, "Wine Gums!")` returns true
- `getTodaysIndex(3)` returns consistent integer 0–2 for same day
- `getUserId()` returns same UUID on repeated calls

---

### Task 6: Frontend UI

**Goal**
Write `docs/index.html` and `docs/style.css` to create a clean, playful quiz interface. `app.js` (started in Task 5) handles all logic.

**Context**
Vanilla HTML/CSS/JS — no framework, no build step. Must work when opened as a static file from GitHub Pages. Users need to set a display name once, then play daily.

**Relevant files / references**
- `docs/app.js` — all logic (Task 5)
- `docs/data/rockbusters.json` and `docs/data/rockbusters-answers.json` (Task 2/5)

**UI sections:**

1. **Name prompt** (shown first time): "What's your name?" input + "Let's go" button. Stores in localStorage.

2. **Quiz card**:
   - Title (e.g. "Sweetbusters")
   - Today's date (British long format: "1 July 2026")
   - 3 clues, each with:
     - Clue number + initials
     - Clue text
     - Text input + "Guess" button (or Enter key)
     - Result line: blank → "Correct!" (green) or "Nope. Not having that." (red)
     - Once correct: input disabled, show tick
   - Prize line (plain text, not bold)
   - "Reveal Answers" button (only shown if not already revealed)
   - Footer: already-revealed state shows answers inline

3. **Answers section** (shown after reveal):
   - "1. Wine Gums: wine gums" format (colon, no em dash)
   - Warning: "You've seen the answers, so no more points today."

4. **Leaderboard** (collapsible or separate tab):
   - Rank, name, total points, today's points in brackets
   - "Refresh" button
   - Fetches from `GET /api/leaderboard`

5. **API URL config**: read from a `<meta name="api-url" content="...">` tag in HTML so it's easy to change for prod without touching JS.

**Style:**
- Clean, readable, slightly playful — not garish
- Works on mobile and desktop
- No external CSS frameworks (vanilla CSS only)
- Colour scheme: muted, easy on the eyes — suggest a warm off-white background, dark text, accent colour for correct answers

**Acceptance criteria**
- `docs/index.html` loads in a browser without a server (open as file)
- Name prompt shows on first load; quiz shows after name set
- Guessing correct answer shows "Correct!" and disables that input
- Guessing wrong shows "Nope. Not having that."
- Reveal button loads answers and calls `/api/reveal`
- Leaderboard section fetches and displays data
- No console errors on page load (with network errors for API calls expected if API not running)
- Page works on mobile viewport (responsive)

---

### Task 7: Tests

**Goal**
Write all tests across five test files. `pytest tests/ -v` must exit 0.

**Relevant files / references**
- `api/scoring.py` — `normalize()`, `check_answer()` (Task 4)
- `api/content_bank.py` — `load_bank()`, `Clue`, `RockbusterSet` (Task 2)
- `api/game_service.py` — `get_set_for_date()` (Task 5)
- `api/db.py` — all db functions (Task 3)
- `api/main.py` — FastAPI app (Task 3)
- `data/rockbusters.yaml` — real file (Task 2)

**Test files:**

`tests/test_normalization.py`:
1. Exact match after normalize
2. Punctuation-insensitive match
3. Alias match
4. Incorrect answer rejected
4b. Empty string → False

`tests/test_content_bank.py`:
5. Missing `prize` raises `ContentBankError`
6. `office_safe: false` raises `ContentBankError`
7. Duplicate `id` raises `ContentBankError`
8. Valid 3-set YAML loads successfully (load real `data/rockbusters.yaml`)

`tests/test_daily_rotation.py`:
9. Same date → same set
10. Consecutive date → different set (3-set bank)
11. Rotation wraps (day offset > bank length cycles back)

`tests/test_scoring.py` (in-memory SQLite):
12. `has_correct_guess` False before record, True after
13. `has_revealed` False before `record_reveal`, True after
14. `get_user_score_today` returns correct count

`tests/test_api.py` (FastAPI TestClient):
15. GET /api/health → 200
16. POST /api/score → 200 first time
17. POST /api/score → 409 second time same clue
18. POST /api/reveal → 200
19. POST /api/score after reveal → 400
20. GET /api/leaderboard → 200 with correct shape

**Constraints:**
- No network calls in tests
- Use in-memory SQLite for db tests
- Use FastAPI TestClient (httpx) for API tests
- Use pytest fixtures for shared setup

**Acceptance criteria**
- `pytest tests/ -v` exits 0
- All 20 test cases exist and pass
- No test requires internet access or a running server

---

### Task 8: Deployment config and export script

**Goal**
Write `api/render.yaml`, complete `scripts/export_json.py`, write `scripts/dry_run.py`, and add a `Procfile` for Render. Configure GitHub Pages to serve from `/docs`.

**Context**
Render free tier can serve a Python web service. GitHub Pages serves the `/docs` folder. The export script must be run before committing frontend changes.

**`api/render.yaml`:**
```yaml
services:
  - type: web
    name: rockbusters-api
    env: python
    buildCommand: pip install -r api/requirements.txt
    startCommand: uvicorn api.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: SQLITE_PATH
        value: /tmp/rockbusters.db
      - key: ROCKBUSTERS_BANK_PATH
        value: data/rockbusters.yaml
      - key: APP_TIMEZONE
        value: Europe/London
```

Note: Render free tier has ephemeral filesystem — SQLite data is lost on restart. Document this in README and note that a persistent disk add-on ($1/mo) or a free Postgres alternative solves it.

**`scripts/export_json.py`:**
- Load YAML via `api.content_bank.load_bank()`
- Write `docs/data/rockbusters.json` — all enabled sets, clues WITHOUT answer/aliases fields
- Write `docs/data/rockbusters-answers.json` — all enabled sets, clues with ONLY number/answer/aliases/reasoning
- Print summary

**`scripts/dry_run.py`:**
- In-memory SQLite
- Load bank
- Get today's set
- Print formatted quiz (title, date, clues)
- Simulate a correct guess (record_guess)
- Simulate a reveal (record_reveal)
- Print answers
- Print leaderboard (empty)
- All output to stdout, no server needed

**Acceptance criteria**
- `python scripts/export_json.py` writes both JSON files without error
- `python scripts/dry_run.py` runs without error and prints sensible output
- `api/render.yaml` is valid YAML
- README documents the ephemeral SQLite issue on Render free tier

---

### Task 9: README and docs

**Goal**
Write `README.md` covering setup, local dev, deployment, and content bank expansion. Write `docs/adding-rockbusters.md`.

**README must cover:**
1. What the app does (2–3 sentences)
2. Architecture overview: GitHub Pages frontend + Render API
3. Local development: install deps, copy .env.example, run API, open index.html
4. Running tests: `pytest tests/ -v`
5. Exporting content to frontend: `python scripts/export_json.py`
6. Deploying to GitHub Pages: enable Pages in repo settings, point to `/docs` folder
7. Deploying API to Render: link repo, set env vars, note free-tier ephemeral SQLite
8. Environment variables table
9. How scoring works
10. How reveal affects scoring
11. Adding Rockbuster sets (link to `docs/adding-rockbusters.md`)
12. Assumptions

**docs/adding-rockbusters.md must cover:**
- Full YAML schema with annotated example
- Content quality rules
- Validation rules
- How to run validation
- How to export to JSON after adding sets
- Suggested topic categories for reaching 730 sets

**Constraints:**
- No mention of Karl, XFM, Ricky, Steve, Pilkington
- No em dashes in example output blocks
- Prize line examples not bold

---

### Task 10: Integration smoke test and fix pass

**Goal**
Run full test suite, run dry_run.py, verify export scripts work, fix any issues, ensure no stubs remain.

**Proposed approach**
1. `pytest tests/ -v` — fix failures
2. `python scripts/export_json.py` — verify both JSON files generated correctly
3. `python scripts/dry_run.py` — verify output sensible
4. Open `docs/index.html` in a browser — verify page loads, name prompt shows, quiz displays
5. Start API with `uvicorn api.main:app --reload`, test all endpoints manually
6. Fix any issues found
7. Ensure no bare `pass` or `TODO` in non-test, non-stub modules
8. Confirm `.gitignore` excludes `.env` and `*.db`
9. Commit everything

**Acceptance criteria**
- `pytest tests/ -v` exits 0
- `python scripts/dry_run.py` prints sensible quiz output
- `docs/index.html` opens in browser without console errors (ignoring API 404s)
- No `TODO` or bare `pass` in `api/` modules
- `git status` shows no `.env` or `*.db` tracked
