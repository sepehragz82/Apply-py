from pydantic import BaseModel

class cityCreate(BaseModel):
    CityName: str
    CountryID: int


class cityUpdate(BaseModel):
    CityName: str
    CountryID: int

class city(BaseModel):
    CityID: int
    CityName: str
    CountryID: int

class Config:
    orm_mode = True