from datetime import datetime

from pydantic import BaseModel


class universityCreate(BaseModel):
    universityName: str
    cityID: int
    internationalsAsTA: bool
    fallDeadline: datetime
    winterDeadline: datetime


class universityUpdate(BaseModel):
    universityName: str
    cityID: int
    internationalsAsTA: bool
    fallDeadline: datetime
    winterDeadline: datetime


class university(BaseModel):
    universityID: int
    universityName: str
    cityID: int
    internationalsAsTA: bool
    fallDeadline: datetime
    winterDeadline: datetime
