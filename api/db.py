"""Rockbusters database initialisation — creates all tables on first run."""

import sqlite3


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
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_version (
                version INTEGER
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

        # Insert schema_version = 1 only on first run (table is empty).
        row = cur.execute("SELECT version FROM schema_version").fetchone()
        if row is None:
            cur.execute("INSERT INTO schema_version (version) VALUES (1)")

        conn.commit()
    finally:
        conn.close()
