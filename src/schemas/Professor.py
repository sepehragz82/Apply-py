from typing import Union

from pydantic import BaseModel


class ProfessorCreate(BaseModel):
    ProfessorFName: str
    ProfessorMName: Union[str, None] = None
    ProfessorLName: str
    ProfGender: Union[bool, None] = None
    ProfCodeinUni: Union[int, None] = None
    UniversityID: int
    DepartmentID: int
    Email: str
    LinkedIN: Union[str, None] = None
    GoogleScholar: Union[str, None] = None
    H_Index: float
    ProfileUniSite: Union[str, None] = None
    EducationDescription: Union[str, None] = None
    ExtraDescription: Union[str, None] = None
    AcademicRankID: int
    
class ProfessorUpdate(BaseModel):
    ProfessorFName: str
    ProfessorMName: Union[str, None] = None
    ProfessorLName: str
    ProfGender: Union[bool, None] = None
    ProfCodeinUni: Union[int, None] = None
    UniversityID: int
    DepartmentID: int
    Email: str
    LinkedIN: Union[str, None] = None
    GoogleScholar: Union[str, None] = None
    H_Index: float
    ProfileUniSite: Union[str, None] = None
    EducationDescription: Union[str, None] = None
    ExtraDescription: Union[str, None] = None
    AcademicRankID: int


class Professor(BaseModel):
    ProfessorID: int
    ProfessorFName: str
    ProfessorMName: Union[str, None] = None
    ProfessorLName: str
    ProfGender: Union[bool, None] = None
    ProfCodeinUni: Union[int, None] = None
    UniversityID: int
    DepartmentID: int
    Email: str
    LinkedIN: Union[str, None] = None
    GoogleScholar: Union[str, None] = None
    H_Index: float
    ProfileUniSite: Union[str, None] = None
    EducationDescription: Union[str, None] = None
    ExtraDescription: Union[str, None] = None
    AcademicRankID: int