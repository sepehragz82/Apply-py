from pydantic import BaseModel

class PositionCreate(BaseModel):
    FundID: int
    PossisionOn: bool
    ProfessorID: int
    DepartmentID: int
    PositionTypeID: int
    PositionYear: int

class PositionUpdate(BaseModel):
    FundID: int
    PossisionOn: bool
    ProfessorID: int
    DepartmentID: int
    PositionTypeID: int
    PositionYear: int

class Position(BaseModel):
    PositionID: int
    FundID: int
    PossisionOn: bool
    ProfessorID: int
    DepartmentID: int
    PositionTypeID: int
    PositionYear: int