from pydantic import BaseModel


class AcademicRankCreate(BaseModel):
    academicRankTitle: str


class AcademicRankUpdate(BaseModel):
    academicRankTitle: str


class AcademicRank(BaseModel):
    academicRankID: int
    academicRankTitle: str


class Config:
    orm_mode = True
