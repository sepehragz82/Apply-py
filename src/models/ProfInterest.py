from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from src.database.session import Base


class prof_interest(Base):
    __tablename__ = "prof_interest"

    ProfResearchInterestID = Column(Integer, primary_key=True, index=True)
    
    ProfessorID = relationship("prof_interest", back_populates="professor")
    ResearchInterestID = relationship("prof_interest", back_populates="research_interest")
