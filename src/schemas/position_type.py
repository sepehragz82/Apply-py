from pydantic import BaseModel


class position_typeCreate(BaseModel):
    positionType: str


class position_typeUpdate(BaseModel):
    positionType: str


class position_type(BaseModel):
    positionTypeID: int
    positionType: str


class Config:
    orm_mode = True
