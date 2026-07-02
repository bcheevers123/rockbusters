"""Rockbusters database initialisation — creates all tables on first run."""

import sqlite3
from datetime import datetime, timezone


def _create_schema(conn: sqlite3.Connection) -> None:
    """Run the schema DDL on *conn*.

    Uses ``CREATE TABLE IF NOT EXISTS`` throughout so this is safe to call on
    an existing connection.  Also records ``schema_version = 1`` on first run.
    """
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER PRIMARY KEY
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id      TEXT PRIMARY KEY,
            display_name TEXT,
            created_at   TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS guesses (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      TEXT    NOT NULL,
            set_id       TEXT    NOT NULL,
            clue_number  INTEGER NOT NULL,
            is_correct   INTEGER NOT NULL,
            guessed_at   TEXT    NOT NULL
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS daily_reveals (
            user_id     TEXT NOT NULL,
            set_id      TEXT NOT NULL,
            reveal_date TEXT NOT NULL,
            PRIMARY KEY (user_id, set_id)
        )
        """
    )

    # Insert schema_version = 1 only on first run; idempotent on re-runs.
    cur.execute("INSERT OR IGNORE INTO schema_version (version) VALUES (1)")

    conn.commit()


def init_db(db_path: str) -> None:
    """Create all application tables in the SQLite database at *db_path*.

    Uses ``CREATE TABLE IF NOT EXISTS`` throughout so this function is safe to
    call on an existing database.  Also records ``schema_version = 1`` the
    first time it runs.

    Args:
        db_path: Path to the SQLite file, or ``':memory:'`` for an in-memory
                 database (useful in tests).
    """
    conn = sqlite3.connect(db_path)
    try:
        _create_schema(conn)
    finally:
        conn.close()


def upsert_user(conn: sqlite3.Connection, user_id: str, display_name: str) -> None:
    """Insert or update a user record.

    If the user already exists, updates the display_name in case it changed.
    """
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """
        INSERT INTO users (user_id, display_name, created_at)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET display_name = excluded.display_name
        """,
        (user_id, display_name, now),
    )
    conn.commit()


def has_revealed(conn: sqlite3.Connection, user_id: str, set_id: str) -> bool:
    """Return True if the user has revealed answers for this set."""
    row = conn.execute(
        "SELECT 1 FROM daily_reveals WHERE user_id = ? AND set_id = ?",
        (user_id, set_id),
    ).fetchone()
    return row is not None


def record_reveal(
    conn: sqlite3.Connection, user_id: str, set_id: str, reveal_date: str
) -> None:
    """Record that a user revealed answers for a set. Idempotent."""
    conn.execute(
        """
        INSERT OR IGNORE INTO daily_reveals (user_id, set_id, reveal_date)
        VALUES (?, ?, ?)
        """,
        (user_id, set_id, reveal_date),
    )
    conn.commit()


def has_correct_guess(
    conn: sqlite3.Connection, user_id: str, set_id: str, clue_number: int
) -> bool:
    """Return True if the user already has a correct guess for this clue."""
    row = conn.execute(
        """
        SELECT 1 FROM guesses
        WHERE user_id = ? AND set_id = ? AND clue_number = ? AND is_correct = 1
        """,
        (user_id, set_id, clue_number),
    ).fetchone()
    return row is not None


def record_guess(
    conn: sqlite3.Connection,
    user_id: str,
    set_id: str,
    clue_number: int,
    is_correct: bool,
) -> None:
    """Record a guess (correct or incorrect) for a user/set/clue."""
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """
        INSERT INTO guesses (user_id, set_id, clue_number, is_correct, guessed_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (user_id, set_id, clue_number, 1 if is_correct else 0, now),
    )
    conn.commit()


def get_user_score_today(
    conn: sqlite3.Connection, user_id: str, set_id: str
) -> int:
    """Return the number of correct guesses the user has for today's set."""
    row = conn.execute(
        """
        SELECT COUNT(*) FROM guesses
        WHERE user_id = ? AND set_id = ? AND is_correct = 1
        """,
        (user_id, set_id),
    ).fetchone()
    return row[0] if row else 0


def get_leaderboard(conn: sqlite3.Connection, limit: int = 10) -> list:
    """Return top users sorted by total correct guesses descending.

    Returns a list of dicts with keys: user_id, display_name, total_points.
    """
    rows = conn.execute(
        """
        SELECT u.user_id, u.display_name, COUNT(g.id) AS total_points
        FROM users u
        LEFT JOIN guesses g
            ON g.user_id = u.user_id AND g.is_correct = 1
        GROUP BY u.user_id, u.display_name
        ORDER BY total_points DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()

    return [
        {
            "user_id": row[0],
            "display_name": row[1],
            "total_points": row[2],
        }
        for row in rows
    ]
