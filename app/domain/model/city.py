from typing import List

from pydantic import BaseModel

from domain.model.track import Track


class City(BaseModel):
    name: str
    temperature: float
    unit: str = "Cº"
    track_list: List[Track] = []
