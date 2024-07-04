from pydantic import BaseModel


class BaseCountry(BaseModel):
    country_name: str


class CountryCreate(BaseCountry):
    pass


class CountryUpdate(BaseCountry):
    pass


class Country(BaseCountry):
    country_id: int

    class Config:
        orm_mode = True
