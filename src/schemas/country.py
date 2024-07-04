from pydantic import BaseModel


class CountryCreate(BaseModel):
    countryName: str


class CountryUpdate(BaseModel):
    countryName: str


class Country(BaseModel):
    countryID: int
    countryName: str

    class Config:
        orm_mode = True
