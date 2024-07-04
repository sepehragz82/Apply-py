from pydantic import BaseModel


class prof_interestCreate(BaseModel):
    professorID: int
    researchInterestID: int


class prof_interestUpdate(BaseModel):
    professorID: int
    researchInterestID: int


class prof_interest(BaseModel):
    profResearchInterestID: int
    professorID: int
    researchInterestID: int
