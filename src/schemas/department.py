from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    departmentName: str


class DepartmentUpdate(BaseModel):
    departmentName: str


class Department(BaseModel):
    departmentID: int
    departmentName: str
