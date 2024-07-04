from datetime import datetime

from pydantic import BaseModel

class universityCreate(BaseModel):
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime

class universityUpdate(BaseModel):
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime

class university(BaseModel):
    UniversityID: int
    UniversityName: str
    CityID: int
    InternationalsAsTA: bool
    FallDeadline: datetime
    WinterDeadline: datetime
