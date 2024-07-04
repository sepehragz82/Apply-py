from pydantic import BaseModel

class fundCreate(BaseModel):
    FundType: str
    
class fundUpdate(BaseModel):
    FundType: str

class fund(BaseModel):
    FundID: int
    FundType: str

class Config:
    orm_mode = True