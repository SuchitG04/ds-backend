from user import router as user_router
from quizzes import router as quizzes_router
from database import create_tables, conn

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    conn.close()


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(quizzes_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

