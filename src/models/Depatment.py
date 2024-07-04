from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class Department(Base):
    __tablename__ = "department"

    departmentID = Column(Integer, primary_key=True)
    departmentName = Column(String)
