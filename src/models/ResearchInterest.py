from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from src.database.session import Base


class research_interest(Base):
    __tablename__ = "research_interest"

    ResearchInterestID = Column(Integer, primary_key=True, index=True)
    ResearchInterestName = Column(String, index=True)
    Description = Column(String, index=True)
