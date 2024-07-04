from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Professor(BaseModel):
    ProfessorID = ProfessorID
    ProfessorFName = ProfessorFName
    ProfessorMName = ProfessorMName
    ProfessorLName = ProfessorLName
    ProfGender = ProfGender
    ProfCodeinUni = ProfCodeinUni
    UniversityID = UniversityID
    DepartmentID = DepartmentID
    Email = Email
    inkedIN =LinkedIN
    GoogleScholar = GoogleScholar
    H_Index = H_Index
    ProfileUniSite = ProfileUniSite
    EducationDescription = EducationDescription
    ExtraDescription = ExtraDescription
    