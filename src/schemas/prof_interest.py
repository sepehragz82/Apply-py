from pydantic import BaseModel


class BaseProfInterest(BaseModel):
    professor_id: int
    research_interest_id: int


class ProfInterestCreate(BaseProfInterest):
    pass


class ProfInterestUpdate(BaseProfInterest):
    pass


class ProfInterest(BaseProfInterest):
    prof_research_interest_id: int
