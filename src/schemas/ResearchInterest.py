
from pydantic import BaseModel

class ResearchInterestCreate(BaseModel):
    ResearchInterestName: str
    Description: str

class ResearchInterestUpdate(BaseModel):
    ResearchInterestName: str
    Description: str

class ResearchInterest(BaseModel):
    ResearchInterestID: int
    ResearchInterestName: str
    Description: str
