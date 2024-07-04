from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base

class Professor(Base):
    __tablename__ = "items"

    ProfessorID = Column(Integer, primary_key=True, index=True)
    ProfessorFName = 
    ProfessorMName =
    ProfessorLName =
    ProfGender =
    ProfCodeinUni =
    UniversityID =
    DepartmentID =
    Email =
    LinkedIN =
    GoogleScholar =
    H_Index =
    ProfileUniSite =
    EducationDescription =
    ExtraDescription =
    AcademicRankID =