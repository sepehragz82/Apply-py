from pydantic import BaseModel

class ProfInterestCreate(BaseModel):
    ProfessorID: int
    ResearchInterestID: int

class ProfInterestUpdate(BaseModel):
    ProfessorID: int
    ResearchInterestID: int

class ProfInterest(BaseModel):
    ProfResearchInterestID: int
    ProfessorID: int
    ResearchInterestID: int
