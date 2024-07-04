from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class ProfInterest(Base):
    __tablename__ = "prof_interest"

    profResearchInterestID = Column(Integer, primary_key=True)

    professorID = relationship("prof_interest", back_populates="professor")
    researchInterestID = relationship(
        "prof_interest", back_populates="research_interest"
    )
