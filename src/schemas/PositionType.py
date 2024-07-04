from pydantic import BaseModel

class position_typeCreate(BaseModel):
    PositionType: str

class position_typeUpdate(BaseModel):
    PositionType: str

class position_type(BaseModel):
    PositionTypeID: int
    PositionType: str

