from pydantic import BaseModel


class research_interestCreate(BaseModel):
    researchInterestName: str
    description: str


class research_interestUpdate(BaseModel):
    researchInterestName: str
    description: str


class research_interest(BaseModel):
    researchInterestID: int
    researchInterestName: str
    description: str
