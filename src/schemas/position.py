from datetime import datetime

from pydantic import BaseModel


class BasePosition(BaseModel):
    fund_id: int
    position_on: bool
    professor_id: int
    department_id: int
    position_type_id: int
    position_year: int


class PositionCreate(BasePosition):
    pass


class PositionUpdate(BasePosition):
    pass


class Position(BasePosition):
    position_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
