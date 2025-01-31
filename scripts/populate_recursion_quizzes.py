import json
from app.database import get_db_connection

def populate_recursion_quizzes():
    """Populate recursion quizzes table with sample data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    quizzes = [
        {
            "question": "What is the base case in a recursive function?",
            "options": [
                "The condition where recursion stops",
                "The first call to the function",
                "The last call to the function",
                "The recursive case"
            ],
            "answer": 0
        },
        {
            "question": "What happens if a recursive function has no base case?",
            "options": [
                "The function will run faster",
                "Stack overflow",
                "Nothing special",
                "The function will return None"
            ],
            "answer": 1
        }
    ]
    
    for quiz in quizzes:
        cursor.execute(
            "INSERT INTO recursion_quizzes (question, options, answer) VALUES (?, ?, ?)",
            (quiz["question"], json.dumps(quiz["options"]), quiz["answer"])
        )
    
    conn.commit()

if __name__ == "__main__":
    populate_recursion_quizzes()
