from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class Professor(Base):
    __tablename__ = "professor"

    professorID = Column(Integer, primary_key=True)
    professorFName = Column(String)
    professorMName = Column(String)
    professorLName = Column(String)
    profGender = Column(Boolean)
    profCodeinUni = Column(Integer)
    universityID = Column(Integer)
    departmentID = Column(Integer)
    email = Column(String)
    linkedIN = Column(String)
    googleScholar = Column(String)
    h_Index = Column(Float)
    profileUniSite = Column(Integer)
    educationDescription = Column(String)
    extraDescription = Column(String)
    academicRankID = Column(Integer)

    universityID = relationship("professor", back_populates="university")
    departmentID = relationship("professor", back_populates="department")
    academicRankID = relationship("professor", back_populates="academicRank")
