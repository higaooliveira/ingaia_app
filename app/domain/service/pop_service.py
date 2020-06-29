from typing import List

from fastapi import HTTPException

from domain.service.abstract_genre_service import AbstractGenreService
from domain.model.city import City
from domain.model.track import Track


class PopService(AbstractGenreService):

    def get_genre_playlist(self, city: City) -> List[Track]:
        if city.temperature > 25:
            track_response = self._spotify_service.search(q='genre:pop', type='track', limit=10)

            return self._normalize_track_list(track_response, 'pop')
        elif self._next_genre_service:
            return self._next_genre_service.get_genre_playlist(city)
        else:
            raise HTTPException(status_code=501, detail="An error occurred while trying to process your request")
