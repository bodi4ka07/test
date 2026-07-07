import os
from contextlib import contextmanager
from typing import Optional
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")


@contextmanager
def get_db_connection():
    """Context manager for database connections."""
    import psycopg2
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_user(user_id: int) -> Optional[dict]:
    """
    Retrieve a user by ID.

    Args:
        user_id: The unique identifier of the user.

    Returns:
        User dict if found, None otherwise.
    """
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, email, created_at FROM users WHERE id = %s",
                (user_id,)
            )
            row = cursor.fetchone()
            if not row:
                return None
            return {"id": row[0], "email": row[1], "created_at": row[2]}


def find_duplicates(items: list) -> list:
    """Return list of duplicate items."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)