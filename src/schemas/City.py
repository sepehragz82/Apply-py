from typing import Optional

from pydantic import BaseModel


class city(BaseModel):
    CityID: int
    CityName: str
    CountryID: int
