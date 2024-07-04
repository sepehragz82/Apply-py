from pydantic import BaseModel

class PositionTypeCreate(BaseModel):
    PositionType: str

class PositionTypeUpdate(BaseModel):
    PositionType: str

class PositionType(BaseModel):
    PositionTypeID: int
    PositionType: str

