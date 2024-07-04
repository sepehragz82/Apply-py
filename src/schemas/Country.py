
from pydantic import BaseModel

class CountryCreate(BaseModel):
    CountryName: str

class CountryUpdate(BaseModel):
    CountryName: str

class Country(BaseModel):
    CountryID: int
    CountryName: str
