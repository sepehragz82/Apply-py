from typing import Optional

from pydantic import BaseModel


class country(BaseModel):
    CountryID: int
    CountryName: str
