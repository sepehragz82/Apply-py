from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class department(Base):
    __tablename__ = "department"

    DepartmentID = Column(Integer, primary_key=True)
    DepartmentName = Column(String)
