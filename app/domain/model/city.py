from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from domain.model.track import Track
from config.database import Base


class CityInDb(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=False, index=True)
    temperature = Column(Float(2), unique=False)
    date = Column(DateTime, unique=False)

    track_list = relationship("TrackInDb", back_populates="city")


class City(BaseModel):
    name: str
    temperature: float
    unit: str = "Cº"
    searched_date: str
    track_list: List[Track] = []

    class Config:
        orm_mode = True
