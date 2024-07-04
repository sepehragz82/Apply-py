from pydantic import BaseModel


class ResearchInterestCreate(BaseModel):
    researchInterestName: str
    description: str


class ResearchInterestUpdate(BaseModel):
    researchInterestName: str
    description: str


class ResearchInterest(BaseModel):
    researchInterestID: int
    researchInterestName: str
    description: str
