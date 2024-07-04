from pydantic import BaseModel


class cityCreate(BaseModel):
    cityName: str
    countryID: int


class cityUpdate(BaseModel):
    cityName: str
    countryID: int


class city(BaseModel):
    cityID: int
    cityName: str
    countryID: int


class Config:
    orm_mode = True
