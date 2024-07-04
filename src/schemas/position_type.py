from pydantic import BaseModel


class BasePositionType(BaseModel):
    position_type: str


class PositionTypeCreate(BasePositionType):
    pass


class PositionTypeUpdate(BasePositionType):
    pass


class PositionType(BasePositionType):
    position_type_id: int

    class Config:
        orm_mode = True
