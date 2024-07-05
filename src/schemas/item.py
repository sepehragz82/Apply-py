from datetime import datetime

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class ItemUpdate(BaseModel):
    name: str


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool | None = None
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
