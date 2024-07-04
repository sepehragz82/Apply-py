from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class Fund(Base):
    __tablename__ = "fund"

    fundID = Column(Integer, primary_key=True)
    fundType = Column(String)
