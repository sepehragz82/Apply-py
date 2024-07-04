from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class fund(Base):
    __tablename__ = "fund"

    FundID = Column(Integer, primary_key=True)
    FundType = Column(String)
