from database import conn
from sqlite3 import DatabaseError
from fastapi import HTTPException, APIRouter

router = APIRouter()


@router.post("/user/{user_id}")
async def create_user(user_id: str):
    try:
        conn.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")


@router.get("/user/{user_id}")
async def get_user(user_id: str):
    try:
        res = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = res.fetchone()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user[0], "queue_score": user[1], "recursion_score": user[2]}


@router.put("/user/{user_id}")
async def update_user_scores(user_id: str, queue_score: int, recursion_score: int):
    try:
        conn.execute(
            "UPDATE users SET queue_score = ?, recursion_score = ? WHERE user_id = ?",
            (queue_score, recursion_score, user_id)
        )
        conn.commit()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")


