import pytest
import json
from app.database import get_db_connection

def test_populate_queue_quizzes(test_db):
    """Test populating queue quizzes"""
    # Import here to avoid circular imports
    from scripts.populate_queue_quizzes import populate_queue_quizzes
    
    # Run population script
    populate_queue_quizzes()
    
    # Verify data was inserted
    cursor = test_db.cursor()
    cursor.execute("SELECT * FROM queue_quizzes")
    quizzes = cursor.fetchall()
    
    assert len(quizzes) > 0
    for quiz in quizzes:
        assert quiz[1]  # question exists
        options = json.loads(quiz[2])
        assert isinstance(options, list)
        assert len(options) > 0
        assert isinstance(quiz[3], int)  # answer is integer

def test_populate_recursion_quizzes(test_db):
    """Test populating recursion quizzes"""
    # Import here to avoid circular imports
    from scripts.populate_recursion_quizzes import populate_recursion_quizzes
    
    # Run population script
    populate_recursion_quizzes()
    
    # Verify data was inserted
    cursor = test_db.cursor()
    cursor.execute("SELECT * FROM recursion_quizzes")
    quizzes = cursor.fetchall()
    
    assert len(quizzes) > 0
    for quiz in quizzes:
        assert quiz[1]  # question exists
        options = json.loads(quiz[2])
        assert isinstance(options, list)
        assert len(options) > 0
        assert isinstance(quiz[3], int)  # answer is integer

def test_populate_videos(test_db):
    """Test populating videos"""
    # Import here to avoid circular imports
    from scripts.populate_videos import populate_videos
    
    # Run population script
    populate_videos()
    
    # Verify data was inserted
    cursor = test_db.cursor()
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    
    assert len(videos) > 0
    for video in videos:
        assert video[1]  # title exists
        assert video[2].startswith("http")  # url is valid

def test_data_consistency(test_db):
    """Test data consistency across all tables"""
    # Import all population scripts
    from scripts.populate_queue_quizzes import populate_queue_quizzes
    from scripts.populate_recursion_quizzes import populate_recursion_quizzes
    from scripts.populate_videos import populate_videos
    
    # Run all population scripts
    populate_queue_quizzes()
    populate_recursion_quizzes()
    populate_videos()
    
    cursor = test_db.cursor()
    
    # Check queue quizzes
    cursor.execute("SELECT COUNT(*) FROM queue_quizzes")
    queue_count = cursor.fetchone()[0]
    assert queue_count > 0
    
    # Check recursion quizzes
    cursor.execute("SELECT COUNT(*) FROM recursion_quizzes")
    recursion_count = cursor.fetchone()[0]
    assert recursion_count > 0
    
    # Check videos
    cursor.execute("SELECT COUNT(*) FROM videos")
    videos_count = cursor.fetchone()[0]
    assert videos_count > 0
    
    # Verify no duplicate IDs
    cursor.execute("SELECT id, COUNT(*) FROM queue_quizzes GROUP BY id HAVING COUNT(*) > 1")
    assert not cursor.fetchall(), "Duplicate IDs found in queue_quizzes"
    
    cursor.execute("SELECT id, COUNT(*) FROM recursion_quizzes GROUP BY id HAVING COUNT(*) > 1")
    assert not cursor.fetchall(), "Duplicate IDs found in recursion_quizzes"
    
    cursor.execute("SELECT id, COUNT(*) FROM videos GROUP BY id HAVING COUNT(*) > 1")
    assert not cursor.fetchall(), "Duplicate IDs found in videos"
