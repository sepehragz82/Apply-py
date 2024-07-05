from datetime import datetime

from pydantic import BaseModel


class BaseFund(BaseModel):
    fund_type: str


class FundCreate(BaseFund):
    pass


class FundUpdate(BaseFund):
    pass


class Fund(BaseFund):
    fund_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
