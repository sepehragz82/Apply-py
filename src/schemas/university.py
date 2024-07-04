from datetime import datetime

from pydantic import BaseModel


class UniversityCreate(BaseModel):
    universityName: str
    cityID: int
    internationalsAsTA: bool
    fallDeadline: datetime
    winterDeadline: datetime


class UniversityUpdate(BaseModel):
    universityName: str
    cityID: int
    internationalsAsTA: bool
    fallDeadline: datetime
    winterDeadline: datetime


class University(BaseModel):
    universityID: int
    universityName: str
    cityID: int
    internationalsAsTA: bool
    fallDeadline: datetime
    winterDeadline: datetime
