
from pydantic import BaseModel

class research_interestCreate(BaseModel):
    ResearchInterestID: int
    ResearchInterestName: str
    Description: str

class research_interestUpdate(BaseModel):
    ResearchInterestName: str
    Description: str



class research_interest(BaseModel):
    ResearchInterestID: int
    ResearchInterestName: str
    Description: str
