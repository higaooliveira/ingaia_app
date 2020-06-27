from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class TrackInDb(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=False, index=True)
    artist = Column(String(200), unique=False)

    city_id = Column(Integer, ForeignKey("city.id"))
    city = relationship("CityInDb", back_populates="track_list")


class Track(BaseModel):
    name: str
    artist: str
