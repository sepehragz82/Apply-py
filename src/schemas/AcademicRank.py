
from pydantic import BaseModel

class AcademicRankCreate(BaseModel):
    AcademicRankTitle: str

class AcademicRankUpdate(BaseModel):
    AcademicRankTitle: str

class AcademicRank(BaseModel):
    AcademicRankID: int
    AcademicRankTitle: str
