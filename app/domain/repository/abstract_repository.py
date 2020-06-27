from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.orm import Session

from config.database import SessionLocal


class AbstractRepository(ABC):

    def __init__(self):
        self._db: Session = SessionLocal()

    @abstractmethod
    def create(self, object: Any):
        """"""

    @abstractmethod
    def get_all(self):
        """"""

    def close_db(self):
        self._db.close()
