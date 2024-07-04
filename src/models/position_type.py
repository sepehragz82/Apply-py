from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from src.database.session import Base


class PositionType(Base):
    __tablename__ = "position_type"

    positionTypeID = Column(Integer, primary_key=True)
    positionType = Column(String)
