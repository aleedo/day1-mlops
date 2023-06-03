from typing import Optional
from pydantic import BaseModel


class SamplePostRequest(BaseModel):
    _id: int
    name: str
