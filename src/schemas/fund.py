from pydantic import BaseModel


class fundCreate(BaseModel):
    fundType: str


class fundUpdate(BaseModel):
    fundType: str


class fund(BaseModel):
    fundID: int
    fundType: str


class Config:
    orm_mode = True
