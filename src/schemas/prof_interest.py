from pydantic import BaseModel


class ProfInterestCreate(BaseModel):
    professorID: int
    researchInterestID: int


class ProfInterestUpdate(BaseModel):
    professorID: int
    researchInterestID: int


class ProfInterest(BaseModel):
    profResearchInterestID: int
    professorID: int
    researchInterestID: int
