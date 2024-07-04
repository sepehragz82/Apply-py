from pydantic import BaseModel


class academic_rankCreate(BaseModel):
    academicRankTitle: str


class academic_rankUpdate(BaseModel):
    academicRankTitle: str


class academic_rank(BaseModel):
    academicRankID: int
    academicRankTitle: str


class Config:
    orm_mode = True
