from pydantic import BaseModel


class BaseProfessor(BaseModel):
    professor_f_name: str
    professor_m_name: str | None = None
    professor_l_name: str
    prof_gender: bool | None = None
    prof_code_in_uni: int | None = None
    university_id: int
    department_id: int
    email: str
    linkedin: str | None = None
    google_scholar: str | None = None
    h_index: float
    profile_uni_site: str | None = None
    education_description: str | None = None
    extra_description: str | None = None
    academic_rank_id: int


class ProfessorCreate(BaseProfessor):
    pass


class ProfessorUpdate(BaseProfessor):
    pass


class Professor(BaseProfessor):
    professor_id: int

    class Config:
        orm_mode = True
