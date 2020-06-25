from fastapi import APIRouter

from src.resources import climatic_playlist

api_router = APIRouter()

api_router.include_router(climatic_playlist.router, tags=["playlist"])
