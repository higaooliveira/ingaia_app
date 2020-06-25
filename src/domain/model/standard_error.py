from pydantic import BaseModel


class StandardError(BaseModel):
    message: str = ""
    status: int = 0
