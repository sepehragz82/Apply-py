from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class research_interest(Base):
    __tablename__ = "research_interest"

    ResearchInterestID = Column(Integer, primary_key=True)
    ResearchInterestName = Column(String)
    Description = Column(String)
