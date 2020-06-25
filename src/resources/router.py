from fastapi import APIRouter

from resources import climatic_playlist

api_router = APIRouter()

api_router.include_router(climatic_playlist.router, tags=["playlist"])
