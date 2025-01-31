import pytest
from fastapi import status

def test_get_queue_quizzes_empty(client):
    """Test getting queue quizzes when none exist"""
    response = client.get("/quizzes/queue")
    assert response.status_code == status.HTTP_200_OK
    quizzes = response.json()
    assert isinstance(quizzes, list)
    assert len(quizzes) == 0

def test_get_recursion_quizzes_empty(client):
    """Test getting recursion quizzes when none exist"""
    response = client.get("/quizzes/recursion")
    assert response.status_code == status.HTTP_200_OK
    quizzes = response.json()
    assert isinstance(quizzes, list)
    assert len(quizzes) == 0

def test_get_queue_quizzes_with_data(client, test_db, sample_quiz_data):
    """Test getting queue quizzes when data exists"""
    # Insert a sample quiz
    cursor = test_db.cursor()
    cursor.execute(
        "INSERT INTO queue_quizzes (question, options, answer) VALUES (?, ?, ?)",
        (sample_quiz_data["question"], sample_quiz_data["options"], sample_quiz_data["answer"])
    )
    test_db.commit()
    
    response = client.get("/quizzes/queue")
    assert response.status_code == status.HTTP_200_OK
    quizzes = response.json()
    assert len(quizzes) == 1
    quiz = quizzes[0]
    assert quiz[1] == sample_quiz_data["question"]  # Index 1 is question
    assert quiz[2] == sample_quiz_data["options"]   # Index 2 is options
    assert quiz[3] == sample_quiz_data["answer"]    # Index 3 is answer

def test_get_recursion_quizzes_with_data(client, test_db, sample_quiz_data):
    """Test getting recursion quizzes when data exists"""
    # Insert a sample quiz
    cursor = test_db.cursor()
    cursor.execute(
        "INSERT INTO recursion_quizzes (question, options, answer) VALUES (?, ?, ?)",
        (sample_quiz_data["question"], sample_quiz_data["options"], sample_quiz_data["answer"])
    )
    test_db.commit()
    
    response = client.get("/quizzes/recursion")
    assert response.status_code == status.HTTP_200_OK
    quizzes = response.json()
    assert len(quizzes) == 1
    quiz = quizzes[0]
    assert quiz[1] == sample_quiz_data["question"]  # Index 1 is question
    assert quiz[2] == sample_quiz_data["options"]   # Index 2 is options
    assert quiz[3] == sample_quiz_data["answer"]    # Index 3 is answer
