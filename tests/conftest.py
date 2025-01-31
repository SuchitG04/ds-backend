import pytest
import sqlite3
from fastapi.testclient import TestClient
from app.main import app
from app.database import set_db_connection, create_tables
import contextlib

@pytest.fixture(scope="function")
def test_db():
    """Create a test database in memory"""
    # Create a new connection for each test
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    
    # Make the connection available globally for the app
    set_db_connection(conn)
    
    # Create tables
    create_tables()
    
    yield conn
    
    # Clean up
    with contextlib.suppress(Exception):
        conn.close()

@pytest.fixture
def client(test_db):
    """Create a test client using the test database"""
    app.dependency_overrides = {}  # Reset any overrides
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "user_id": "test_user_1",
        "user_name": "Test User",
        "queue_score": 0,
        "recursion_score": 0
    }

@pytest.fixture
def sample_quiz_data():
    """Sample quiz data for testing"""
    return {
        "question": "Test Question",
        "options": '["A", "B", "C", "D"]',
        "answer": 0
    }
