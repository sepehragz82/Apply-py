from datetime import datetime

from pydantic import BaseModel

class UniversityCreate(BaseModel):
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime

class UniversityUpdate(BaseModel):
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime

class University(BaseModel):
    UniversityID: int
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime
