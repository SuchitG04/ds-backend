from app.user import router as user_router
from app.quizzes import router as quizzes_router
from app.vid_content import router as vid_content_router
from app.database import create_tables, get_db_connection

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager"""
    try:
        # Initialize database on startup
        create_tables()
        yield
    finally:
        # Clean up database connection on shutdown
        conn = get_db_connection()
        if conn is not None:
            conn.close()


app = FastAPI(lifespan=lifespan)

# Add CORS middleware first
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex=None,
    expose_headers=[],
    max_age=600,
)

# Add routers
app.include_router(user_router)
app.include_router(quizzes_router)
app.include_router(vid_content_router)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Hello World!"}
