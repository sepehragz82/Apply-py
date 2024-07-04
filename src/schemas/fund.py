from pydantic import BaseModel


class FundCreate(BaseModel):
    fundType: str


class FundUpdate(BaseModel):
    fundType: str


class Fund(BaseModel):
    fundID: int
    fundType: str


class Config:
    orm_mode = True
