from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class Professor(Base):
    __tablename__ = "professor"

    ProfessorID = Column(Integer, primary_key=True)
    ProfessorFName = Column(String)
    ProfessorMName = Column(String)
    ProfessorLName = Column(String)
    ProfGender = Column(bool)
    ProfCodeinUni = Column(int)
    UniversityID = Column(int)
    DepartmentID = Column(int)
    Email = Column(String)
    LinkedIN = Column(String)
    GoogleScholar = Column(String)
    H_Index = Column(float)
    ProfileUniSite = Column(int)
    EducationDescription = Column(String)
    ExtraDescription = Column(String)
    AcademicRankID = Column(int)

    UniversityID = relationship("Professor", back_populates="University")
    DepartmentID = relationship("Professor", back_populates="Department")
    AcademicRankID = relationship("Professor", back_populates="AcademicRank")
