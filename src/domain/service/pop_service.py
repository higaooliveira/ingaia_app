from domain.service.abstract_genre_service import AbstractGenreService
from domain.model.city import City


class PopService(AbstractGenreService):

    def get_genre_playlist(self, city: City):
        if city.temperature > 25:
            """do something"""
        else:
            return self._next_genre_service.get_genre_playlist(city)
