from pydantic import BaseModel


class positionCreate(BaseModel):
    fundID: int
    posisionOn: bool
    professorID: int
    departmentID: int
    positionTypeID: int
    positionYear: int


class positionUpdate(BaseModel):
    fundID: int
    possisionOn: bool
    professorID: int
    departmentID: int
    positionTypeID: int
    positionYear: int


class position(BaseModel):
    positionID: int
    fundID: int
    possisionOn: bool
    professorID: int
    departmentID: int
    positionTypeID: int
    positionYear: int
