from domain.service.abstract_genre_service import AbstractGenreService
from domain.model.city import City


class RockService(AbstractGenreService):

    def get_genre_playlist(self, city: City):
        if 10 <= city.temperature <= 25:
            """do something"""
        else:
            return self._next_genre_service.get_genre_playlist(city)
