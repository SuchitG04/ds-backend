from database import conn
from sqlite3 import DatabaseError
from fastapi import HTTPException, APIRouter

router = APIRouter()


@router.get("/users")
async def get_all_users():
    try:
        res = conn.execute("SELECT * FROM users")
        users = res.fetchall()
        return users
    except DatabaseError as d:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(d)}")


@router.post("/user/{user_id}")
async def create_user(user_id: str, user_name: str):
    try:
        conn.execute(
            "INSERT OR IGNORE INTO users (user_id, user_name) VALUES (?, ?)",
            (user_id, user_name),
        )
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


@router.put("/user/{user_id}/{table}")
async def update_score(user_id: str, table: str, score: int = 0):
    if table not in ["recursion", "queue"]:
        raise HTTPException(status_code=400, detail="Invalid table name")
    try:
        query = f"UPDATE users SET {table}_score = ? WHERE user_id = ?"
        conn.execute(
            query,
            (score, user_id),
        )
        conn.commit()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
