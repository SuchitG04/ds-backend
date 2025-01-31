from sqlite3 import DatabaseError
from fastapi import APIRouter, HTTPException
import logging
from app.database import get_db_connection

router = APIRouter()

@router.get("/videos")
async def get_videos():
    """Get all videos"""
    try:
        conn = get_db_connection()
        res = conn.execute("SELECT * FROM videos")
        videos = res.fetchall()
        return videos if videos else []
    except DatabaseError as e:
        logging.error(f"Database error in get_videos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error in get_videos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")