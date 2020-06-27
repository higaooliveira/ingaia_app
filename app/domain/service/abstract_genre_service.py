from abc import ABC, abstractmethod
from typing import List

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from fastapi import HTTPException

from domain.model.city import City
from domain.model.track import Track


class AbstractGenreService(ABC):

    _spotify_service = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    def __init__(self, next_genre_service=None):
        self._next_genre_service = next_genre_service

    @abstractmethod
    def get_genre_playlist(self, city: City) -> List[Track]:
        """This is an abstract method, it isn't not implemented here"""

    def _normalize_track_list(self, track_response) -> List[Track]:
        track_list = []

        if not track_response['tracks']['items']:
            raise HTTPException(status_code=404, detail="Music list not found for the searched genre")

        for track_info in track_response['tracks']['items']:
            track_list.append(Track(name=track_info['name'], artist=track_info['artists'][0]['name']))

        return track_list
