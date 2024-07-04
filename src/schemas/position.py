from pydantic import BaseModel

class positionCreate(BaseModel):
    ProfResearchInterestID: int
    ProfessorID: int
    ResearchInterestID: int

class positionUpdate(BaseModel):
    ProfessorID: int
    ResearchInterestID: int


class position(BaseModel):
    ProfResearchInterestID: int
    ProfessorID: int
    ResearchInterestID: int