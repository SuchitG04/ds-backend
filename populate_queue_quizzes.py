import sqlite3
import json

def main():
    # List of questions, each entry is a dictionary
    questions = [
        {
            "question": "Which of the following is the correct operation to insert an element in a queue?",
            "options": ["enqueue", "dequeue", "push", "pop"],
            "answer": "enqueue"
        },
        {
            "question": "Which of the following is the correct operation to remove an element from a queue?",
            "options": ["enqueue", "dequeue", "push", "pop"],
            "answer": "dequeue"
        },
        {
            "question": "Which of the following best describes a queue data structure?",
            "options": ["Last-in first-out", "First-in first-out", "First-in last-out", "None of the above"],
            "answer": "First-in first-out"
        },
        {
            "question": "What is the time complexity of an enqueue operation in a queue implemented using an array (assuming no resizing overhead)?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "answer": "O(1)"
        },
        {
            "question": "What operation returns the element at the front of the queue without removing it?",
            "options": ["peek", "front", "top", "pop"],
            "answer": "peek"
        },
        {
            "question": "Which queue variation allows insertion at one end and deletion from both ends?",
            "options": ["Priority queue", "Deque (Double-ended queue)", "Circular queue", "Multi-level queue"],
            "answer": "Deque (Double-ended queue)"
        },
        {
            "question": "When a queue is implemented using an array, which problem can occur even if the array isn't fully occupied?",
            "options": ["Overflow", "Underflow", "Dequeue error", "False overflow"],
            "answer": "False overflow"
        },
        {
            "question": "What is a common application of queues in operating systems?",
            "options": ["Function call management", "Process scheduling", "Recursion stack", "Memory allocation"],
            "answer": "Process scheduling"
        },
        {
            "question": "Which queue data structure ensures that the element with the highest priority is always served first?",
            "options": ["Circular queue", "Priority queue", "Multi-queue", "None of the above"],
            "answer": "Priority queue"
        },
        {
            "question": "What is the time complexity of checking if a queue is empty?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "answer": "O(1)"
        }
    ]

    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queue_quizzes (
            id INTEGER PRIMARY KEY,
            question TEXT,
            options TEXT,  -- stored as JSON
            answer TEXT
        )
    ''')

    # Insert questions
    for i, q in enumerate(questions, start=1):
        cursor.execute('''
            INSERT INTO queue_quizzes (id, question, options, answer)
            VALUES (?, ?, ?, ?)
        ''', (i, q["question"], json.dumps(q["options"]), q["answer"]))

    # Commit and close
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
