from pydantic import BaseModel

class positionCreate(BaseModel):
    FundID: int
    PossisionOn: bool
    ProfessorID: int
    DepartmentID: int
    PositionTypeID: int
    PositionYear: int

class positionUpdate(BaseModel):
    FundID: int
    PossisionOn: bool
    ProfessorID: int
    DepartmentID: int
    PositionTypeID: int
    PositionYear: int

class position(BaseModel):
    PositionID: int
    FundID: int
    PossisionOn: bool
    ProfessorID: int
    DepartmentID: int
    PositionTypeID: int
    PositionYear: int