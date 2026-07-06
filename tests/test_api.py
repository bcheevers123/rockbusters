"""Tests for the FastAPI endpoints using TestClient.

We patch the Config before importing app so that:
  - SQLITE_PATH points to a temp file (not :memory: because main.py closes the
    connection after each request, which is fine for a file db)
  - ROCKBUSTERS_BANK_PATH points to the real data/rockbusters.yaml
No network calls are made.
"""

import os
import tempfile
import importlib
import sys

import pytest
from fastapi.testclient import TestClient


# ---------------------------------------------------------------------------
# Fixture: temp db + TestClient
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def client():
    """
    Build a TestClient pointing at the real app.

    We create a fresh temporary SQLite file for the test session so tests
    run in isolation from the production database.  The bank path points
    to the real YAML so today-endpoint tests have real data.
    """
    # Resolve bank path relative to this file
    bank_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "data", "rockbusters.yaml")
    )

    # Create a temp SQLite file for this test session
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    os.close(db_fd)

    # Set env vars BEFORE importing api.main so Config picks them up.
    # Remove stale cached modules so the app re-initialises cleanly.
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]

    os.environ["SQLITE_PATH"] = db_path
    os.environ["ROCKBUSTERS_BANK_PATH"] = bank_path

    from api.main import app

    with TestClient(app) as c:
        yield c

    # Cleanup
    os.unlink(db_path)
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]


# Stable user/display for tests that don't need isolated state.
TEST_USER_ID = "test-user-api"
TEST_DISPLAY = "API Tester"

# Unique user IDs for tests that set up their own preconditions so they don't
# depend on execution order and don't interfere with each other.
USER_409 = "test-user-409"
USER_400 = "test-user-400"
USER_REVEAL = "test-user-reveal"


def _get_set_id(client: TestClient) -> str:
    """Fetch today's set_id from the /api/today endpoint."""
    resp = client.get("/api/today")
    assert resp.status_code == 200
    return resp.json()["set_id"]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_health(client):
    """GET /api/health returns 200 and {status: ok}."""
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_score_first_time_200(client):
    """POST /api/score → 200 on first correct guess."""
    set_id = _get_set_id(client)
    resp = client.post(
        "/api/score",
        json={
            "user_id": TEST_USER_ID,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
            "clue_number": 1,
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("ok") is True
    assert "points_today" in body


def test_score_second_time_409(client):
    """POST /api/score → 409 when the same clue is submitted twice."""
    set_id = _get_set_id(client)
    # Precondition: submit the score once first so the second attempt gets 409.
    first = client.post(
        "/api/score",
        json={
            "user_id": USER_409,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
            "clue_number": 1,
        },
    )
    assert first.status_code == 200
    # Second submission of the same clue must be rejected.
    resp = client.post(
        "/api/score",
        json={
            "user_id": USER_409,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
            "clue_number": 1,
        },
    )
    assert resp.status_code == 409


def test_reveal_200(client):
    """POST /api/reveal → 200."""
    set_id = _get_set_id(client)
    resp = client.post(
        "/api/reveal",
        json={
            "user_id": USER_REVEAL,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
        },
    )
    assert resp.status_code == 200
    assert resp.json().get("ok") is True


def test_score_after_reveal_400(client):
    """POST /api/score after reveal → 400."""
    set_id = _get_set_id(client)
    # Precondition: reveal first so the subsequent score attempt is rejected.
    reveal = client.post(
        "/api/reveal",
        json={
            "user_id": USER_400,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
        },
    )
    assert reveal.status_code == 200
    # Scoring after reveal must be rejected.
    resp = client.post(
        "/api/score",
        json={
            "user_id": USER_400,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
            "clue_number": 2,
        },
    )
    assert resp.status_code == 400


def test_leaderboard_200(client):
    """GET /api/leaderboard → 200 with a 'leaderboard' key."""
    resp = client.get("/api/leaderboard")
    assert resp.status_code == 200
    body = resp.json()
    assert "leaderboard" in body


def test_today_200_no_answers(client):
    """GET /api/today → 200; response has set_id and clues; clues have no 'answer'."""
    resp = client.get("/api/today")
    assert resp.status_code == 200
    body = resp.json()
    assert "set_id" in body
    assert "clues" in body
    for clue in body["clues"]:
        assert "answer" not in clue
        assert "aliases" not in clue


def test_user_status_200(client):
    """GET /api/user-status?user_id=X&set_id=Y → 200."""
    set_id = _get_set_id(client)
    resp = client.get(
        "/api/user-status",
        params={"user_id": TEST_USER_ID, "set_id": set_id},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert "revealed" in body
    assert "correct_clues" in body
    assert "points_today" in body


# ---------------------------------------------------------------------------
# Sheets mode: startup rebuild test (mocked)
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Sheets mode: startup rebuild test (mocked)
# ---------------------------------------------------------------------------

def test_sheets_mode_leaderboard_uses_replayed_data():
    """When Sheets env vars are set, startup replays Sheets data into in-memory SQLite.
    The leaderboard endpoint should return data from the replayed db."""
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
    del os.environ["ROCKBUSTERS_BANK_PATH"]
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]


def test_sheets_mode_score_calls_write_through():
    """In Sheets mode, POST /api/score should call sheets_write_with_retry for upsert and guess."""
    import sys
    from unittest.mock import MagicMock, patch

    bank_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "data", "rockbusters.yaml")
    )

    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]

    fake_sheets_data = {"users": [], "guesses": [], "daily_reveals": []}
    mock_client = MagicMock()

    os.environ["GOOGLE_SHEETS_ID"] = "FAKE_SHEET_ID"
    os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"] = '{"type":"service_account"}'
    os.environ["ROCKBUSTERS_BANK_PATH"] = bank_path

    with patch("api.sheets.get_sheets_client", return_value=mock_client), \
         patch("api.sheets.load_all", return_value=fake_sheets_data), \
         patch("api.sheets.sheets_write_with_retry") as mock_write:
        from api.main import app
        from fastapi.testclient import TestClient
        # get today's set_id first
        with TestClient(app) as c:
            today = c.get("/api/today").json()
            set_id = today["set_id"]
            clue_number = today["clues"][0]["number"]
            resp = c.post("/api/score", json={
                "user_id": "u_wt",
                "display_name": "WriteThrough",
                "set_id": set_id,
                "clue_number": clue_number,
            })
            assert resp.status_code == 200
            assert mock_write.call_count >= 2  # upsert_user + append_guess

    del os.environ["GOOGLE_SHEETS_ID"]
    del os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
    del os.environ["ROCKBUSTERS_BANK_PATH"]
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]


def test_sheets_mode_reveal_calls_write_through():
    """In Sheets mode, POST /api/reveal should call sheets_write_with_retry."""
    import sys
    from unittest.mock import MagicMock, patch

    bank_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "data", "rockbusters.yaml")
    )

    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]

    fake_sheets_data = {"users": [], "guesses": [], "daily_reveals": []}
    mock_client = MagicMock()

    os.environ["GOOGLE_SHEETS_ID"] = "FAKE_SHEET_ID"
    os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"] = '{"type":"service_account"}'
    os.environ["ROCKBUSTERS_BANK_PATH"] = bank_path

    with patch("api.sheets.get_sheets_client", return_value=mock_client), \
         patch("api.sheets.load_all", return_value=fake_sheets_data), \
         patch("api.sheets.sheets_write_with_retry") as mock_write:
        from api.main import app
        from fastapi.testclient import TestClient
        with TestClient(app) as c:
            today = c.get("/api/today").json()
            set_id = today["set_id"]
            resp = c.post("/api/reveal", json={
                "user_id": "u_rv",
                "display_name": "RevealUser",
                "set_id": set_id,
            })
            assert resp.status_code == 200
            assert mock_write.call_count >= 2  # upsert_user + append_reveal

    del os.environ["GOOGLE_SHEETS_ID"]
    del os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
    del os.environ["ROCKBUSTERS_BANK_PATH"]
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]


def test_sheets_mode_startup_failure_falls_back_to_file_sqlite(tmp_path):
    """When Sheets startup fails, app falls back to file SQLite and stays up."""
    import sys
    from unittest.mock import MagicMock, patch

    bank_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "data", "rockbusters.yaml")
    )
    db_path = str(tmp_path / "test.db")

    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]

    os.environ["GOOGLE_SHEETS_ID"] = "FAKE_SHEET_ID"
    os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"] = '{"type":"service_account"}'
    os.environ["ROCKBUSTERS_BANK_PATH"] = bank_path
    os.environ["SQLITE_PATH"] = db_path

    with patch("api.sheets.get_sheets_client", side_effect=Exception("credentials invalid")):
        from api.main import app
        from fastapi.testclient import TestClient
        with TestClient(app) as c:
            resp = c.get("/api/health")
            assert resp.status_code == 200

    for key in ["GOOGLE_SHEETS_ID", "GOOGLE_SERVICE_ACCOUNT_JSON", "ROCKBUSTERS_BANK_PATH", "SQLITE_PATH"]:
        os.environ.pop(key, None)
    for mod_name in list(sys.modules.keys()):
        if mod_name.startswith("api"):
            del sys.modules[mod_name]
