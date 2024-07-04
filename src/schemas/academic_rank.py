from pydantic import BaseModel


class BaseAcademicRank(BaseModel):
    academic_rank_title: str


class AcademicRankCreate(BaseAcademicRank):
    pass


class AcademicRankUpdate(BaseAcademicRank):
    pass


class AcademicRank(BaseAcademicRank):
    academic_rank_id: int

    class Config:
        orm_mode = True
