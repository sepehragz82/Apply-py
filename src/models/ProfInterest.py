from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from src.database.session import Base


class prof_interest(Base):
    __tablename__ = "prof_interest"

    ProfResearchInterestID = Column(Integer, primary_key=True, index=True)
    ProfessorID = Column(ForeignKey, index=True)
    ResearchInterestID = Column(ForeignKey, index=True)

    author_id = relationship("User", back_populates="notes")
