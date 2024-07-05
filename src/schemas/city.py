from datetime import datetime

from pydantic import BaseModel


class BaseCity(BaseModel):
    city_name: str
    country_id: int


class CityCreate(BaseCity):
    pass


class CityUpdate(BaseCity):

    pass


class City(BaseCity):
    city_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
