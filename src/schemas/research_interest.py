from pydantic import BaseModel


class BaseResearchInterest(BaseModel):
    research_interest_name: str
    description: str


class ResearchInterestCreate(BaseResearchInterest):
    pass


class ResearchInterestUpdate(BaseResearchInterest):
    pass


class ResearchInterest(BaseResearchInterest):
    research_interest_id: int

    class Config:
        orm_mode = True
