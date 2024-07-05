from datetime import datetime

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
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
