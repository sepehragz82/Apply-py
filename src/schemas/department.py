from datetime import datetime

from pydantic import BaseModel


class BaseDepartment(BaseModel):
    department_name: str


class DepartmentCreate(BaseDepartment):
    pass


class DepartmentUpdate(BaseDepartment):
    pass


class Department(BaseDepartment):
    department_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
