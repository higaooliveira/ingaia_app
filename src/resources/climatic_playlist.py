from fastapi import APIRouter, HTTPException
from requests import HTTPError
from src.domain.service.http_client import HttpClient
from src.domain.service.playlist_service import PlaylistService


router = APIRouter()

# @router.get("/heartbeat", response_model=HearbeatResult, name="heartbeat")
@router.get("/playlist/")
def get_playlist(city: str = ""):
    try:
        playlist_service = PlaylistService(HttpClient())

        return playlist_service.get_city_info(city)

    except HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.reason,
        )
