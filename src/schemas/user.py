from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    name: str
    password: str


class UserUpdate(BaseModel):
    username: str
    name: str
    bio: str


class PasswordUpdate(BaseModel):
    password: str
    new_password: str


class User(BaseModel):
    id: int
    username: str
    name: str
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
