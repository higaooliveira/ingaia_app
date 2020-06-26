from domain.service.http_client import HttpClient
from domain.model.city import City
from domain.service.rock_service import RockService
from domain.service.pop_service import PopService
from domain.service.classic_service import ClassicService


class PlaylistService:
    API_WEATHER_KEY = "my-fake-token"
    API_WEATHER_BASE_URL = "my-fake-token"
    API_KEY_SPOTIFY = "my-fake-token"

    def __init__(self, http_client: HttpClient):
        self._http_client = http_client
        self._http_client.base_url = self.API_WEATHER_BASE_URL

    def __get_city_info(self, city: str):
        response = self._http_client.get('/weather', params={"q": city,
                                                             "appid": self.API_WEATHER_KEY,
                                                             "units": "metric"})

        return City(name=response['name'], temperature=response['main']['temp'])

    def get_playlist(self, city: str):
        city = self.__get_city_info(city)

        genre_service = ClassicService(RockService(PopService()))

        return genre_service.get_genre_playlist(city)
