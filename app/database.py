import sqlite3
from typing import Optional
from contextlib import contextmanager

# Global connection object
conn: Optional[sqlite3.Connection] = None

def get_db_connection():
    """Get the current database connection"""
    global conn
    if conn is None:
        conn = sqlite3.connect("app.db", check_same_thread=False)
    return conn

def set_db_connection(new_conn: sqlite3.Connection):
    """Set a new database connection (useful for testing)"""
    global conn
    conn = new_conn

def create_tables():
    """Create all necessary database tables"""
    connection = get_db_connection()
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                user_name TEXT,
                queue_score INTEGER DEFAULT 0,
                recursion_score INTEGER DEFAULT 0
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS queue_quizzes (
                id INTEGER PRIMARY KEY,
                question TEXT,
                options TEXT, -- JSON type
                answer INTEGER
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS recursion_quizzes (
                id INTEGER PRIMARY KEY,
                question TEXT,
                options TEXT, -- JSON type
                answer INTEGER
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                title TEXT,
                url TEXT
            )
            """
        )
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
