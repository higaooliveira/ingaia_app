from typing import List

from domain.service.abstract_genre_service import AbstractGenreService
from domain.model.city import City
from domain.model.track import Track


class RockService(AbstractGenreService):

    def get_genre_playlist(self, city: City) -> List[Track]:
        if 10 <= city.temperature <= 25:
            track_response = self._spotify_service.search(q='genre:rock-n-roll', type='track', limit=10)

            return self._normalize_track_list(track_response)

        return self._next_genre_service.get_genre_playlist(city)
