from pydantic import BaseModel


class BaseFund(BaseModel):
    fund_type: str


class FundCreate(BaseFund):
    pass


class FundUpdate(BaseFund):
    pass


class Fund(BaseFund):
    fund_id: int

    class Config:
        orm_mode = True
