import sqlite3

conn = sqlite3.connect('app.db')

def create_tables():
    try:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                queue_score INTEGER NULL,
                recursion_score INTEGER NULL
            )
            '''
        )

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS queue_quizzes (
                id INTEGER PRIMARY KEY,
                question TEXT,
                options TEXT, -- JSON type
                answer INTEGER
            )
            '''
        )

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS recursion_quizzes (
                id INTEGER PRIMARY KEY,
                question TEXT,
                options TEXT, -- JSON type
                answer INTEGER
            )
            '''
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

