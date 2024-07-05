from datetime import datetime

from pydantic import BaseModel


class BaseAcademicRank(BaseModel):
    academic_rank_title: str


class AcademicRankCreate(BaseAcademicRank):
    pass


class AcademicRankUpdate(BaseAcademicRank):
    pass


class AcademicRank(BaseAcademicRank):
    academic_rank_id: int
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
