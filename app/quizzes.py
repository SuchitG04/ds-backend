from database import conn
from sqlite3 import DatabaseError
from fastapi import HTTPException, APIRouter

router = APIRouter()


@router.get("/quizzes/queue")
async def get_queue_quiz():
    try:
        res = conn.execute("SELECT * FROM queue_quizzes")
        quizzes = res.fetchall()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")

    if quizzes is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return quizzes


@router.get("/quizzes/recursion")
async def get_recursion_quiz():
    try:
        res = conn.execute("SELECT * FROM recursion_quizzes")
        quizzes = res.fetchall()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")

    if quizzes is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return quizzes