from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class ResearchInterest(Base):
    __tablename__ = "research_interest"

    researchInterestID = Column(Integer, primary_key=True)
    researchInterestName = Column(String)
    description = Column(String)
