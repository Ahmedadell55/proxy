from fastapi import FastAPI
from contextlib import asynccontextmanager
from chat import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server started ✅")
    yield
    print("Server stopped ")

app = FastAPI(
    title="Mental Health Chatbot",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {"message": "OK"}

app.include_router(router, prefix="/api", tags=["Chat"])