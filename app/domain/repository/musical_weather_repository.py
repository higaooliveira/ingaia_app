from datetime import datetime

from domain.model.city import CityInDb, City
from domain.repository.abstract_repository import AbstractRepository
from domain.model.track import TrackInDb

class MusicalWeatherRepository(AbstractRepository):

    def get_all(self):
        return self._db.query(CityInDb).all()

    def create(self, city: City) -> CityInDb:
        city_db = CityInDb(name=city.name, temperature=city.temperature, date=datetime.now())
        city_db.track_list = [TrackInDb(name=track.name, artist=track.artist) for track in city.track_list]
        self._db.add(city_db)
        self._db.commit()
        self._db.refresh(city_db)

        return city_db
