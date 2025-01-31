from fastapi import status

def test_get_videos_empty(client):
    """Test getting videos when none exist"""
    response = client.get("/videos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_videos_with_data(client, test_db):
    """Test getting videos when data exists"""
    # Insert a sample video
    cursor = test_db.cursor()
    cursor.execute(
        "INSERT INTO videos (title, url) VALUES (?, ?)",
        ("Test Video", "https://example.com/video")
    )
    test_db.commit()

    response = client.get("/videos")
    assert response.status_code == status.HTTP_200_OK
    videos = response.json()
    assert len(videos) == 1
    assert videos[0][1] == "Test Video"  # title
    assert videos[0][2] == "https://example.com/video"  # url

def test_get_videos_error_handling(client, test_db):
    """Test error handling when database operation fails"""
    # Drop the videos table to simulate a database error
    cursor = test_db.cursor()
    cursor.execute("DROP TABLE videos")
    test_db.commit()

    response = client.get("/videos")
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert "Error in DB" in response.json()["detail"]
