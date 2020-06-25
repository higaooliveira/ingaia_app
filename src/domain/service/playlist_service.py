from src.domain.service.http_client import HttpClient
from src.domain.model.city import City
from src.domain.service.rock_service import RockService
from src.domain.service.pop_service import PopService
from src.domain.service.classic_service import ClassicService


class PlaylistService:
    API_WEATHER_KEY = "47ab211f0f5a3f89151850edee950e3f"
    API_WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5"
    API_KEY_SPOTIFY = "BQC-pDD25Gf9SaU5-Viyim3HWzEz1Hd-6Co1r0jsV7AtFgmrsxaklA4-u5TG0qoODWoEqEgvT_SvLpx-WbXdIYWGzHCS_8D-asvzLncmc6cRbVDvxcCGzWZkZmjnTJOmrKLILWUuA5pP2_iE77dV3vtXJfjkjxI_KajSZ6y_aRQmuM_1-PzaWuK8UMJH4bsdEaZCavkSPeBWy78t_lcoVQHa-qnUD_g3cioY9sbgEMYOvjmfYjD2n5LQ1QUkvjHkYb12Hlu7cV-JXiwsUPEVK2YjdXPeRIBT"

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
