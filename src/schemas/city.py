from pydantic import BaseModel


class CityCreate(BaseModel):
    cityName: str
    countryID: int


class CityUpdate(BaseModel):
    cityName: str
    countryID: int


class City(BaseModel):
    cityID: int
    cityName: str
    countryID: int

    class Config:
        orm_mode = True
