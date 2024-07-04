from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class position_type(Base):
    __tablename__ = "position_type"

    PositionTypeID = Column(Integer, primary_key=True)
    PositionType = Column(String)
