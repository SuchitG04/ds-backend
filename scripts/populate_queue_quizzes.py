import json
from app.database import get_db_connection

def populate_queue_quizzes():
    """Populate queue quizzes table with sample data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    quizzes = [
        {
            "question": "What is the time complexity of enqueue operation in a queue?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
            "answer": 0
        },
        {
            "question": "Which of the following is not a type of queue?",
            "options": ["Priority Queue", "Circular Queue", "Binary Queue", "Double Ended Queue"],
            "answer": 2
        }
    ]
    
    for quiz in quizzes:
        cursor.execute(
            "INSERT INTO queue_quizzes (question, options, answer) VALUES (?, ?, ?)",
            (quiz["question"], json.dumps(quiz["options"]), quiz["answer"])
        )
    
    conn.commit()

if __name__ == "__main__":
    populate_queue_quizzes()
