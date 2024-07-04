from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class Professor(Base):
    __tablename__ = "professor"

    professorID = Column(Integer, primary_key=True)
    professorFName = Column(String)
    professorMName = Column(String)
    professorLName = Column(String)
    profGender = Column(bool)
    profCodeinUni = Column(int)
    universityID = Column(int)
    departmentID = Column(int)
    email = Column(String)
    linkedIN = Column(String)
    googleScholar = Column(String)
    h_Index = Column(float)
    profileUniSite = Column(int)
    educationDescription = Column(String)
    extraDescription = Column(String)
    academicRankID = Column(int)

    universityID = relationship("professor", back_populates="university")
    departmentID = relationship("professor", back_populates="department")
    academicRankID = relationship("professor", back_populates="academicRank")
