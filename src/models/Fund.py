from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from src.database.session import Base


class fund(Base):
    __tablename__ = "fund"

    FundID = Column(Integer, primary_key=True, index=True)
    FundType = Column(String, index=True)
