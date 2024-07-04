
from pydantic import BaseModel

class cityCreate(BaseModel):
    CityID: int
    CityName: str
    CountryID: int


class cityUpdate(BaseModel):
    CityName: str


class city(BaseModel):
    CityID: int
    CityName: str
    CountryID: int
