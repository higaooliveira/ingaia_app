from os import environ

from domain.service.http_client import HttpClient
from domain.model.city import City
from domain.service.rock_service import RockService
from domain.service.pop_service import PopService
from domain.service.classic_service import ClassicService


class MusicalWeatherService:
    API_WEATHER_KEY = environ['API_WEATHER_KEY']
    API_WEATHER_BASE_URL = environ['API_WEATHER_BASE_URL']

    def __init__(self, http_client: HttpClient):
        self._http_client = http_client
        self._http_client.base_url = self.API_WEATHER_BASE_URL

    def get_playlist(self, city: str) -> City:
        city = self.__get_city_info(city)

        genre_service = ClassicService(RockService(PopService()))
        city.track_list = genre_service.get_genre_playlist(city)

        return city

    def __get_city_info(self, city: str) -> City:
        response = self._http_client.get('/weather', params={"q": city,
                                                             "appid": self.API_WEATHER_KEY,
                                                             "units": "metric"})

        return City(name=response['name'], temperature=response['main']['temp'])
