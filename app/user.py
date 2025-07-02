from sqlite3 import DatabaseError
from fastapi import APIRouter, HTTPException
import logging
from .database import get_db_connection

router = APIRouter()


@router.get("/users")
async def get_all_users():
    """Get all users"""
    try:
        conn = get_db_connection()
        res = conn.execute("SELECT * FROM users")
        users = res.fetchall()
        return users if users else []
    except DatabaseError as e:
        logging.error(f"Database error in get_all_users: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in get_all_users: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.post("/user/{user_id}")
async def create_user(user_id: str, user_name: str):
    """Create a new user"""
    try:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (user_id, user_name) VALUES (?, ?)",
            (user_id, user_name),
        )
        conn.commit()
        return {"status": "success"}
    except DatabaseError as e:
        logging.error(f"Database error in create_user: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in create_user: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/user/{user_id}")
async def get_user(user_id: str):
    """Get a user by ID"""
    try:
        conn = get_db_connection()
        res = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = res.fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "user_id": user[0],
            "user_name": user[1],
            "queue_score": user[2],
            "recursion_score": user[3]
        }
    except HTTPException:
        raise
    except DatabaseError as e:
        logging.error(f"Database error in get_user: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in get_user: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.put("/user/{user_id}/{table}")
async def update_score(user_id: str, table: str, score: int = 0):
    """Update a user's score"""
    if table not in ["recursion", "queue"]:
        raise HTTPException(status_code=400, detail="Invalid table name")
    try:
        conn = get_db_connection()
        query = f"UPDATE users SET {table}_score = ? WHERE user_id = ?"
        conn.execute(query, (score, user_id))
        conn.commit()
        return {"status": "success"}
    except DatabaseError as e:
        logging.error(f"Database error in update_score: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in update_score: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
