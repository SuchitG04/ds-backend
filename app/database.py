import sqlite3

conn = sqlite3.connect('app.db')

def create_tables():
    try:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY,
                name TEXT,
                score INTEGER
            )
            '''
        )

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                leaderboard_id INTEGER,
                FOREIGN KEY(leaderboard_id) REFERENCES leaderboard(id)
            )
            '''
        )

        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS stack_quizzes (
                id INTEGER PRIMARY KEY,
                question TEXT,
                options TEXT, -- JSON type
                answer TEXT
            )
            '''
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e


def initialize_database():
    create_tables()
