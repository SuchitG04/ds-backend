from fastapi import status
import pytest
from app.database import get_db_connection

def test_root_endpoint(client):
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World!"}

def test_cors_headers(client):
    """Test CORS headers are properly set"""
    test_origin = "http://example.com"
    response = client.options("/", headers={
        "Origin": test_origin,
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "Content-Type",
    })
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["access-control-allow-origin"] == test_origin
    assert response.headers["access-control-allow-credentials"] == "true"
    assert "GET" in response.headers["access-control-allow-methods"]
    assert "Content-Type" in response.headers["access-control-allow-headers"]

def test_database_lifecycle(client):
    """Test database connection lifecycle"""
    # Test database connection is initialized
    conn = get_db_connection()
    assert conn is not None
    
    # Test tables are created
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    
    assert "users" in table_names
    assert "queue_quizzes" in table_names
    assert "recursion_quizzes" in table_names
    assert "videos" in table_names

def test_full_user_workflow(client):
    """Test complete user workflow"""
    user_data = {
        "user_id": "test_user",
        "user_name": "Test User"
    }
    
    # Create user
    response = client.post(f"/user/{user_data['user_id']}", params={"user_name": user_data["user_name"]})
    assert response.status_code == status.HTTP_200_OK
    
    # Get user
    response = client.get(f"/user/{user_data['user_id']}")
    assert response.status_code == status.HTTP_200_OK
    user = response.json()
    assert user["user_id"] == user_data["user_id"]
    assert user["user_name"] == user_data["user_name"]
    assert user["queue_score"] == 0
    assert user["recursion_score"] == 0
    
    # Update queue score
    response = client.put(f"/user/{user_data['user_id']}/queue", params={"score": 42})
    assert response.status_code == status.HTTP_200_OK
    
    # Verify updated score
    response = client.get(f"/user/{user_data['user_id']}")
    assert response.status_code == status.HTTP_200_OK
    user = response.json()
    assert user["queue_score"] == 42
