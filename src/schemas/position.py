from pydantic import BaseModel


class PositionCreate(BaseModel):
    fundID: int
    positionOn: bool
    professorID: int
    departmentID: int
    positionTypeID: int
    positionYear: int


class PositionUpdate(BaseModel):
    fundID: int
    positionOn: bool
    professorID: int
    departmentID: int
    positionTypeID: int
    positionYear: int


class Position(BaseModel):
    positionID: int
    fundID: int
    positionOn: bool
    professorID: int
    departmentID: int
    positionTypeID: int
    positionYear: int
