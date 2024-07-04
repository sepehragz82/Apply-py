from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from src.database.session import Base


class academic_rank(Base):
    __tablename__ = "academic_rank"

    AcademicRankID = Column(Integer, primary_key=True, index=True)
    AcademicRankTitle = Column(String, index=True)
