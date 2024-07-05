from datetime import datetime

from pydantic import BaseModel


class BaseUniversity(BaseModel):
    university_name: str
    city_id: int
    internationals_as_ta: bool
    fall_deadline: datetime
    winter_deadline: datetime


class UniversityCreate(BaseUniversity):
    pass


class UniversityUpdate(BaseUniversity):
    pass


class University(BaseUniversity):
    university_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
