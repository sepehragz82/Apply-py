from pydantic import BaseModel


class countryCreate(BaseModel):
    countryName: str


class countryUpdate(BaseModel):
    countryName: str


class country(BaseModel):
    countryID: int
    countryName: str


class Config:
    orm_mode = True
