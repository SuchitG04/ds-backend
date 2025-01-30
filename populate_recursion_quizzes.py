import sqlite3
import json

def main():
    # List of questions, each entry is a dictionary
    questions = [
        {
            "question": "Which statement best describes recursion?",
            "options": [
                "A function that calls itself",
                "A function that loops indefinitely",
                "A function with a single return statement",
                "A function with multiple parameters"
            ],
            "answer": "A function that calls itself"
        },
        {
            "question": "What is a base case in recursion?",
            "options": [
                "A case that increases recursion depth",
                "A case that stops the recursion",
                "A case that triggers an error",
                "A case that uses a loop"
            ],
            "answer": "A case that stops the recursion"
        },
        {
            "question": "Which data structure is used by most programming languages to implement function calls and recursion?",
            "options": ["Queue", "Stack", "Array", "Tree"],
            "answer": "Stack"
        },
        {
            "question": "Which of the following is an advantage of using recursion?",
            "options": [
                "It always uses less memory",
                "It can simplify the code and make it more readable",
                "It makes code run faster in all cases",
                "It prevents stack overflow"
            ],
            "answer": "It can simplify the code and make it more readable"
        },
        {
            "question": "Which of the following problems is often solved using recursion?",
            "options": [
                "Sorting an array using Bubble Sort",
                "Calculating the factorial of a number",
                "Finding the shortest path in a graph with Dijkstra's algorithm",
                "Implementing a queue"
            ],
            "answer": "Calculating the factorial of a number"
        },
        {
            "question": "In recursion, what happens if the base case is never reached?",
            "options": [
                "The function executes successfully and returns 0",
                "The program switches to an iterative approach automatically",
                "The program runs into an infinite recursive call leading to a stack overflow",
                "The program will still execute, but produce a wrong answer"
            ],
            "answer": "The program runs into an infinite recursive call leading to a stack overflow"
        },
        {
            "question": "Which term describes reducing a problem into smaller subproblems that resemble the original?",
            "options": [
                "Memoization",
                "Iteration",
                "Divide and conquer",
                "Recurrence"
            ],
            "answer": "Divide and conquer"
        },
        {
            "question": "What is a recursive function’s general structure in most programming languages?",
            "options": [
                "A function with no parameters and a global variable",
                "A function calling itself and a condition to stop calling itself",
                "A function with only a while loop",
                "A function that returns a string"
            ],
            "answer": "A function calling itself and a condition to stop calling itself"
        },
        {
            "question": "Which of the following is generally not a typical use case for recursion?",
            "options": [
                "Traversing a tree",
                "Calculating the nth Fibonacci number",
                "Implementing factorial",
                "Looping over a static array in a straightforward manner"
            ],
            "answer": "Looping over a static array in a straightforward manner"
        },
        {
            "question": "When converting a recursive function into an iterative one, which data structure is commonly used to simulate recursion’s behavior?",
            "options": ["Queue", "Linked list", "Stack", "Heap"],
            "answer": "Stack"
        }
    ]

    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recursion_quizzes (
            id INTEGER PRIMARY KEY,
            question TEXT,
            options TEXT,  -- stored as JSON
            answer TEXT
        )
    ''')

    # Insert questions
    for i, q in enumerate(questions, start=1):
        cursor.execute('''
            INSERT INTO recursion_quizzes (id, question, options, answer)
            VALUES (?, ?, ?, ?)
        ''', (i, q["question"], json.dumps(q["options"]), q["answer"]))

    # Commit changes and close
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
