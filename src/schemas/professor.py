from typing import Union

from pydantic import BaseModel


class professorCreate(BaseModel):
    professorFName: str
    professorMName: Union[str, None] = None
    professorLName: str
    profGender: Union[bool, None] = None
    profCodeinUni: Union[int, None] = None
    universityID: int
    departmentID: int
    email: str
    linkedIN: Union[str, None] = None
    googleScholar: Union[str, None] = None
    h_Index: float
    profileUniSite: Union[str, None] = None
    educationDescription: Union[str, None] = None
    extraDescription: Union[str, None] = None
    academicRankID: int


class professorUpdate(BaseModel):
    professorFName: str
    professorMName: Union[str, None] = None
    professorLName: str
    profGender: Union[bool, None] = None
    profCodeinUni: Union[int, None] = None
    universityID: int
    departmentID: int
    email: str
    linkedIN: Union[str, None] = None
    googleScholar: Union[str, None] = None
    h_Index: float
    profileUniSite: Union[str, None] = None
    educationDescription: Union[str, None] = None
    extraDescription: Union[str, None] = None
    academicRankID: int


class professor(BaseModel):
    professorID: int
    professorFName: str
    professorMName: Union[str, None] = None
    professorLName: str
    profGender: Union[bool, None] = None
    profCodeinUni: Union[int, None] = None
    universityID: int
    departmentID: int
    email: str
    linkedIN: Union[str, None] = None
    googleScholar: Union[str, None] = None
    h_Index: float
    profileUniSite: Union[str, None] = None
    educationDescription: Union[str, None] = None
    extraDescription: Union[str, None] = None
    academicRankID: int
