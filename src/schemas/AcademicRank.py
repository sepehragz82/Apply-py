
from pydantic import BaseModel

class academic_rankCreate(BaseModel):
    AcademicRankID: int
    AcademicRankTitle: str


class academic_rankUpdate(BaseModel):
    AcademicRankTitle: str



class academic_rank(BaseModel):
    AcademicRankID: int
    AcademicRankTitle: str
