from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class academic_rank(Base):
    __tablename__ = "academic_rank"

    AcademicRankID = Column(Integer, primary_key=True)
    AcademicRankTitle = Column(String)
