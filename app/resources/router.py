from fastapi import APIRouter

from resources import musical_weather

api_router = APIRouter()

api_router.include_router(musical_weather.router, tags=["playlist"])
