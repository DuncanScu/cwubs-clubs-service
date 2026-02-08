from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router

app = FastAPI(title="Clubs Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "healthy", "service": "clubs"}

app.include_router(api_router)
