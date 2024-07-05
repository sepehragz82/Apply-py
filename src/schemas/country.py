from datetime import datetime

from pydantic import BaseModel


class BaseCountry(BaseModel):
    country_name: str


class CountryCreate(BaseCountry):
    pass


class CountryUpdate(BaseCountry):
    pass


class Country(BaseCountry):
    country_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
