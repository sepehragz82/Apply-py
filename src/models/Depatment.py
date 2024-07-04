from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from src.database.session import Base


class department(Base):
    __tablename__ = "department"

    DepartmentID = Column(Integer, primary_key=True, index=True)
    DepartmentName = Column(String, index=True)