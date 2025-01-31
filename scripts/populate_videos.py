from app.database import get_db_connection

def populate_videos():
    """Populate videos table with sample data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    videos = [
        {
            "title": "Introduction to Queues",
            "url": "https://www.youtube.com/watch?v=queue_intro"
        },
        {
            "title": "Understanding Recursion",
            "url": "https://www.youtube.com/watch?v=recursion_basics"
        }
    ]
    
    for video in videos:
        cursor.execute(
            "INSERT INTO videos (title, url) VALUES (?, ?)",
            (video["title"], video["url"])
        )
    
    conn.commit()

if __name__ == "__main__":
    populate_videos()
