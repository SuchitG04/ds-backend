import pytest
from fastapi import status

def test_create_user(client, sample_user_data):
    """Test user creation"""
    response = client.post(
        f"/user/{sample_user_data['user_id']}",
        params={"user_name": sample_user_data["user_name"]}
    )
    assert response.status_code == status.HTTP_200_OK

def test_get_user(client, sample_user_data):
    """Test user retrieval"""
    # First create a user
    client.post(
        f"/user/{sample_user_data['user_id']}",
        params={"user_name": sample_user_data["user_name"]}
    )
    
    # Then get the user
    response = client.get(f"/user/{sample_user_data['user_id']}")
    assert response.status_code == status.HTTP_200_OK
    user = response.json()
    assert user["user_id"] == sample_user_data["user_id"]

def test_get_nonexistent_user(client):
    """Test getting a user that doesn't exist"""
    response = client.get("/user/nonexistent")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_user_score(client, sample_user_data):
    """Test updating user scores"""
    # Create user first
    client.post(
        f"/user/{sample_user_data['user_id']}",
        params={"user_name": sample_user_data["user_name"]}
    )
    
    # Update queue score
    score = 42
    response = client.put(
        f"/user/{sample_user_data['user_id']}/queue",
        params={"score": score}
    )
    assert response.status_code == status.HTTP_200_OK
    
    # Verify score was updated
    response = client.get(f"/user/{sample_user_data['user_id']}")
    user = response.json()
    assert user["queue_score"] == score

def test_update_invalid_score_type(client, sample_user_data):
    """Test updating score with invalid table name"""
    # Create user first
    client.post(
        f"/user/{sample_user_data['user_id']}",
        params={"user_name": sample_user_data["user_name"]}
    )
    
    response = client.put(
        f"/user/{sample_user_data['user_id']}/invalid",
        params={"score": 42}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
