# Rockbusters

A daily cryptic-initials quiz web app. Each day a new set of three clues rotates in — players guess the answers, score points, and compete on a leaderboard. No login required.

The app is split into a static frontend (GitHub Pages) and a lightweight Python API (Render). Content lives in a YAML file that is exported to JSON for the frontend.

---

## Architecture

```
GitHub Pages (docs/)
  index.html + app.js + style.css
  docs/data/rockbusters.json        -- clues (no answers)
  docs/data/rockbusters-answers.json -- answers + aliases

Render (api/)
  FastAPI + SQLite
  Handles scoring, leaderboard, reveal state
```

The frontend reads today's set directly from the JSON files bundled with the site. The API is only called when a player submits a guess, reveals answers, or loads the leaderboard. This means the app works (read-only) even if the API is down.

---

## Local development

**1. Install Python dependencies**

```bash
pip install -r api/requirements.txt
```

**2. Create a `.env` file**

```bash
cp .env.example .env
```

Edit `.env` and set values (see [Environment variables](#environment-variables) below). All variables have defaults so you can skip this step for a quick start.

**3. Run the API**

```bash
uvicorn api.main:app --reload
```

The API listens on `http://localhost:8000`.

**4. Open the frontend**

Open `docs/index.html` directly in a browser. The `meta[name="api-url"]` tag is blank by default, which tells `app.js` to use `http://localhost:8000`.

---

## Running tests

```bash
python -m pytest tests/ -v
```

The test suite covers content bank validation, daily rotation, answer normalisation, scoring rules, and API endpoints.

---

## Exporting content to the frontend

After editing `data/rockbusters.yaml`, regenerate the JSON files:

```bash
python scripts/export_json.py
```

This writes:
- `docs/data/rockbusters.json` — clues only (no answers)
- `docs/data/rockbusters-answers.json` — answers, aliases, and reasoning

Only enabled sets are exported. Commit both files alongside the YAML change.

---

## Deploying to GitHub Pages

1. Push the repo to GitHub.
2. Go to repo **Settings** > **Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Set branch to `main`, folder to `/docs`. Save.

GitHub will serve the site from the `docs/` folder. The URL will be `https://<username>.github.io/<repo>/`.

After deploying the API (see below), set the API URL in `docs/index.html`:

```html
<meta name="api-url" content="https://your-api.onrender.com">
```

Commit and push. The frontend will now point at the live API.

---

## Deploying the API to Render

1. Create a new **Web Service** on [Render](https://render.com).
2. Connect your GitHub repository.
3. Set **Build command**: `pip install -r api/requirements.txt`
4. Set **Start command**: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (see table below).

A `render.yaml` is included in `api/render.yaml` for reference, but Render's dashboard is the recommended way to configure the service.

**SQLite on Render free tier:** Render's free tier has an ephemeral filesystem. The SQLite database is lost every time the service restarts. To persist scores across restarts, add Render's disk add-on ($1/month), mount it at `/data`, and set `SQLITE_PATH=/data/rockbusters.db`.

---

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `SQLITE_PATH` | `rockbusters.db` | Path to the SQLite database file |
| `ROCKBUSTERS_BANK_PATH` | `data/rockbusters.yaml` | Path to the YAML content bank |
| `APP_TIMEZONE` | `Europe/London` | Timezone used for daily set rotation |
| `ALLOWED_ORIGINS` | `*` | CORS allowed origins (comma-separated or `*`) |
| `API_SECRET` | _(empty)_ | Reserved for future auth. Not enforced yet. |

---

## How scoring works

Each set has three clues. A player earns 1 point per correct answer, up to a maximum of 3 points per day.

- Submitting a correct answer calls `POST /api/score` and records the guess.
- A clue can only be scored once per player per set.
- Points accumulate on the leaderboard across all days.

---

## How reveal affects scoring

Pressing "Reveal answers" calls `POST /api/reveal`, which records that the player has seen the answers for that set. After revealing:

- Further scoring is blocked for that set (`POST /api/score` returns HTTP 400).
- This is enforced server-side, not just in the UI.

Revealing is idempotent — calling it multiple times has no additional effect.

---

## Adding Rockbuster sets

See [docs/adding-rockbusters.md](docs/adding-rockbusters.md) for the full guide, including the YAML schema, content rules, and how to validate and export new sets.

---

## API reference

| Method | Path | Description |
|---|---|---|
| `GET` | `/api/health` | Health check |
| `GET` | `/api/today` | Today's set (clues only, no answers) |
| `GET` | `/api/leaderboard` | Top 10 players, includes today's points |
| `POST` | `/api/score` | Record a correct answer |
| `POST` | `/api/reveal` | Record that a user revealed answers |
| `GET` | `/api/user-status` | User's state for a given set (`?user_id=X&set_id=Y`) |

`GET /api/today` returns clues without answers, making it suitable for Slack or Discord bot integrations.

---

## Assumptions

- **User identity** is a UUID generated in the browser and stored in `localStorage`. There is no login system. Clearing browser storage resets the player's local identity (scores in the database are retained but unlinked from the new UUID).
- **Render free tier** restarts the service periodically, which wipes the SQLite database unless a persistent disk is attached.
- **Answers are loaded on demand.** The answers JSON file is only fetched when a player submits a guess or reveals answers — it is not loaded on page load.
- **`/api/today`** returns today's set from the API (live timezone-aware rotation) and is available for future bot integrations without needing to replicate the rotation logic client-side.
