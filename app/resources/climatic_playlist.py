from fastapi import APIRouter, HTTPException
from requests import HTTPError
from app.domain.service.http_client import HttpClient
from app.domain.service.playlist_service import PlaylistService


router = APIRouter()

# @router.get("/heartbeat", response_model=HearbeatResult, name="heartbeat")
class MusicalWeatherController:

    @router.get("/playlist/")
    def get_playlist(city: str = ""):
        try:
            playlist_service = PlaylistService(HttpClient())

            return playlist_service.get_playlist(city)

        except HTTPError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.reason,
            )
