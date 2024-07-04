from typing import Union

from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class ItemUpdate(BaseModel):
    name: str

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Config:
    orm_mode = True
