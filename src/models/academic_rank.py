from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class AcademicRank(Base):
    __tablename__ = "academic_rank"

    academicRankID = Column(Integer, primary_key=True)
    academicRankTitle = Column(String)
