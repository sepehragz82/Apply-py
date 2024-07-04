from typing import Union

from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    departmentName: str


class DepartmentUpdate(BaseModel):
    departmentName: str


class Department(BaseModel):
    departmentID: int
    departmentName: str

    class Config:
        orm_mode = True
