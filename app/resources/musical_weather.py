from json import loads

from fastapi import APIRouter, HTTPException
from requests import HTTPError

from domain.model.city import City
from domain.service.http_client import HttpClient
from domain.service.musical_weather_service import MusicalWeatherService


router = APIRouter()


class MusicalWeatherController:

    @router.get("/musical_weather/", response_model=City, name="Returns a list of songs suggested by weather")
    def get_playlist(city: str = ""):
        try:
            musical_weather = MusicalWeatherService(HttpClient())

            return musical_weather.get_playlist(city)

        except HTTPError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=loads(e.response.text)['message'],
            )

        except Exception:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while trying to process your request",
            )
