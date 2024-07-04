
from pydantic import BaseModel

class countryCreate(BaseModel):
    CountryName: str

class countryUpdate(BaseModel):
    CountryName: str

class country(BaseModel):
    CountryID: int
    CountryName: str
