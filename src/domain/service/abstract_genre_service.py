from abc import ABC, abstractmethod
from src.domain.model.city import City


class AbstractGenreService(ABC):

    def __init__(self, next_genre_service):
        self._next_genre_service = next_genre_service

    @abstractmethod
    def get_genre_playlist(self, city: City):
        """This is an abstract method, it isn't not implemented here"""
