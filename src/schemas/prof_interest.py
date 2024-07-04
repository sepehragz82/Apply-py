from pydantic import BaseModel

class prof_interestCreate(BaseModel):
    ProfessorID: int
    ResearchInterestID: int

class prof_interestUpdate(BaseModel):
    ProfessorID: int
    ResearchInterestID: int

class prof_interest(BaseModel):
    ProfResearchInterestID: int
    ProfessorID: int
    ResearchInterestID: int
