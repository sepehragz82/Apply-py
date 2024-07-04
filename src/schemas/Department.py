from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    DepartmentName: str

class DepartmentUpdate(BaseModel):
    DepartmentName: str
    
class Department(BaseModel):
    DepartmentID: int
    DepartmentName: str