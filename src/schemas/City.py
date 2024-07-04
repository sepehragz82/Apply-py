
from pydantic import BaseModel

class CityCreate(BaseModel):
    CityName: str
    CountryID: int

class CityUpdate(BaseModel):
    CityName: str
    CountryID: int

class City(BaseModel):
    CityID: int
    CityName: str
    CountryID: int
