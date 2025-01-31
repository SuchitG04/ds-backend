from sqlite3 import DatabaseError
from fastapi import APIRouter, HTTPException
import logging
from app.database import get_db_connection

router = APIRouter()

@router.get("/quizzes/queue")
async def get_queue_quiz():
    """Get all queue quizzes"""
    try:
        conn = get_db_connection()
        res = conn.execute("SELECT * FROM queue_quizzes")
        quizzes = res.fetchall()
        return quizzes if quizzes else []
    except DatabaseError as e:
        logging.error(f"Database error in get_queue_quiz: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in get_queue_quiz: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@router.get("/quizzes/recursion")
async def get_recursion_quiz():
    """Get all recursion quizzes"""
    try:
        conn = get_db_connection()
        res = conn.execute("SELECT * FROM recursion_quizzes")
        quizzes = res.fetchall()
        return quizzes if quizzes else []
    except DatabaseError as e:
        logging.error(f"Database error in get_recursion_quiz: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in get_recursion_quiz: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")