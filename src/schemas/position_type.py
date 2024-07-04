from pydantic import BaseModel


class PositionTypeCreate(BaseModel):
    positionType: str


class PositionTypeUpdate(BaseModel):
    positionType: str


class PositionType(BaseModel):
    positionTypeID: int
    positionType: str


class Config:
    orm_mode = True
