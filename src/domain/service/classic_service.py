from src.domain.service.abstract_genre_service import AbstractGenreService
from src.domain.model.city import City


class ClassicService(AbstractGenreService):

    def get_genre_playlist(self, city: City):
        if city.temperature < 10:
            """do something"""
        else:
            return self._next_genre_service.get_genre_playlist(city)
