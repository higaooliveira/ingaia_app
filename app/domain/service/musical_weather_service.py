from os import environ
from datetime import datetime

from fastapi import HTTPException

from domain.service.http_client import HttpClient
from domain.model.city import City
from domain.model.track import Track
from domain.service.rock_service import RockService
from domain.service.pop_service import PopService
from domain.service.classic_service import ClassicService
from domain.repository.musical_weather_repository import MusicalWeatherRepository
from domain.repository.abstract_repository import AbstractRepository


class MusicalWeatherService:
    API_WEATHER_KEY = environ['API_WEATHER_KEY']
    API_WEATHER_BASE_URL = environ['API_WEATHER_BASE_URL']

    def __init__(self, http_client: HttpClient, repository: AbstractRepository = MusicalWeatherRepository()):
        self._repository = repository
        self._http_client = http_client
        self._http_client.base_url = self.API_WEATHER_BASE_URL

    def get_playlist(self, city: str) -> City:
        city = self.__get_city_info(city)

        genre_service = ClassicService(RockService(PopService()))
        city.track_list = genre_service.get_genre_playlist(city)

        self._repository.create(city)

        return city

    def get_all_searched_cities(self):
        cities = self._repository.get_all()

        if not cities:
            raise HTTPException(
                status_code=404,
                detail="Cities not found",
            )

        return [
            City(
                name=city.name,
                temperature=city.temperature,
                searched_date=city.date.strftime("%d/%m/%Y %H:%M:%S"),
                track_list=[Track(name=track.name, artist=track.artist) for track in city.track_list]
            ) for city in cities
        ]

    def __get_city_info(self, city: str) -> City:
        response = self._http_client.get('/weather', params={"q": city,
                                                             "appid": self.API_WEATHER_KEY,
                                                             "units": "metric"})

        return City(
            name=response['name'],
            temperature=response['main']['temp'],
            searched_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
