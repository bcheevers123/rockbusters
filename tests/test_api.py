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


# We need a stable set_id and user across multiple tests in sequence.
# Use module-level state so tests that depend on prior state can share it.
TEST_USER_ID = "test-user-api"
TEST_DISPLAY = "API Tester"


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
    resp = client.post(
        "/api/score",
        json={
            "user_id": TEST_USER_ID,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
            "clue_number": 1,  # same clue as test_score_first_time_200
        },
    )
    assert resp.status_code == 409


def test_reveal_200(client):
    """POST /api/reveal → 200."""
    set_id = _get_set_id(client)
    resp = client.post(
        "/api/reveal",
        json={
            "user_id": TEST_USER_ID,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
        },
    )
    assert resp.status_code == 200
    assert resp.json().get("ok") is True


def test_score_after_reveal_400(client):
    """POST /api/score after reveal → 400."""
    set_id = _get_set_id(client)
    resp = client.post(
        "/api/score",
        json={
            "user_id": TEST_USER_ID,
            "display_name": TEST_DISPLAY,
            "set_id": set_id,
            "clue_number": 2,  # a different clue, but reveal already happened
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
