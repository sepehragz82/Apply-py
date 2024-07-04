from pydantic import BaseModel

class departmentCreate(BaseModel):
    DepartmentName: str

class departmentUpdate(BaseModel):
    DepartmentName: str
    
class department(BaseModel):
    DepartmentID: int
    DepartmentName: str