from datetime import datetime

from pydantic import BaseModel

class UniversityTypeCreate(BaseModel):
    UniversityID: int
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime

class position_typeUpdate(BaseModel):
    UniversityID: int
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime


class position_type(BaseModel):
    UniversityID: int
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime
