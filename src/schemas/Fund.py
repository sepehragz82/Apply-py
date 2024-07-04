from pydantic import BaseModel

class FundCreate(BaseModel):
    FundType: str
    
class FundUpdate(BaseModel):
    FundType: str

class Fund(BaseModel):
    FundID: int
    FundType: str

