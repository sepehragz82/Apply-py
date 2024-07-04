from pydantic import BaseModel

class fundCreate(BaseModel):
    FundID: int
    FundType: str


class fundUpdate(BaseModel):
    FundType: str



class fund(BaseModel):
    FundID: int
    FundType: str

