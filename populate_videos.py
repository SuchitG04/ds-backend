import sqlite3
from sqlite3 import DatabaseError

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        title TEXT,
        url TEXT
    )
''')

try:
    conn.execute(
        "INSERT INTO videos (title, url) VALUES (?, ?)",
        ("Circular Queue Operations", "https://www.youtube.com/watch?v=vu6xBl7ReiU")
    )
    conn.execute(
        "INSERT INTO videos (title, url) VALUES (?, ?)",
        ("Recursion - Fibonacci Series", "https://www.youtube.com/watch?v=uHP3OdUI0SQ")
    )
    conn.commit()
except DatabaseError as e:
    conn.rollback()
    raise e

conn.close()