import pytest
from sqlite3 import DatabaseError
from app.database import create_tables

def test_create_tables(test_db):
    """Test that tables are created successfully"""
    # Tables should already be created by the fixture
    cursor = test_db.cursor()
    
    # Check if all tables exist
    tables = ["users", "queue_quizzes", "recursion_quizzes", "videos"]
    for table in tables:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        assert cursor.fetchone() is not None, f"Table {table} was not created"

def test_table_schema(test_db):
    """Test that tables have correct schema"""
    cursor = test_db.cursor()
    
    # Test users table schema
    cursor.execute("PRAGMA table_info(users)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    assert "user_id" in columns
    assert "user_name" in columns
    assert "queue_score" in columns
    assert "recursion_score" in columns
    
    # Test queue_quizzes table schema
    cursor.execute("PRAGMA table_info(queue_quizzes)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    assert "question" in columns
    assert "options" in columns
    assert "answer" in columns

def test_database_rollback(test_db):
    """Test that database rolls back on error"""
    cursor = test_db.cursor()
    
    # Try to create a table with invalid SQL
    with pytest.raises(DatabaseError):
        cursor.execute("CREATE TABLE invalid_table (id INTEGER PRIMARY KEY,")
        test_db.commit()
    
    # Verify the invalid table wasn't created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='invalid_table'")
    assert cursor.fetchone() is None
