from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from chat import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Server started ✅")
    yield
    print("🛑 Server stopped")

app = FastAPI(
    title="Mental Health Chatbot API",
    version="1.0.0",
    lifespan=lifespan
)

# =====================================================
# =====================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # React dev
        "http://localhost:5173",      # Vite dev
        "http://127.0.0.1:5500",      # Live Server
        "*",                         
    ],
    allow_credentials=True,
    allow_methods=["*"],              
    allow_headers=["*"],               )

@app.get("/")
def root():
    return {
        "message": "Mental Health Chatbot API is running 🧠",
        "status": "active",
        "endpoints": {
            "chat": "/api/chat",
            "docs": "/docs"
        }
    }

app.include_router(router, prefix="/api", tags=["Chat"])
