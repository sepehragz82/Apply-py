from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from src.database.session import Base


class position_type(Base):
    __tablename__ = "position_type"

    PositionTypeID = Column(Integer, primary_key=True, index=True)
    PositionType = Column(String, index=True)
