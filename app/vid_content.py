from database import conn
from sqlite3 import DatabaseError

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/videos")
async def get_videos():
    try:
        res = conn.execute("SELECT * FROM videos")
        videos = res.fetchall()
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=f"Error in DB: {str(e)}")

    if videos is None:
        raise HTTPException(status_code=404, detail="Videos not found")

    return videos