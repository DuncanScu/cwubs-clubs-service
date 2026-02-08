from fastapi import APIRouter

from app.api.clubs import router as clubs_router

api_router = APIRouter()


api_router.include_router(clubs_router)

