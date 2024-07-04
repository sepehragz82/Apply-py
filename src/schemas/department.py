from pydantic import BaseModel


class departmentCreate(BaseModel):
    departmentName: str


class departmentUpdate(BaseModel):
    departmentName: str


class department(BaseModel):
    departmentID: int
    departmentName: str
