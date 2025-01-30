from user import router as user_router
from database import create_tables, conn

from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    conn.close()


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

