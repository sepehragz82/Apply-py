from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class Position(Base):
    __tablename__ = "position"

    positionID = Column(Integer, primary_key=True)
    positionOn = Column(Boolean)
    positionYear = Column(Integer)

    professorID = relationship("position", back_populates="professor")
    fundID = relationship("position", back_populates="fund")
    positionTypeID = relationship("position", back_populates="position_type")
    departmentID = relationship("position", back_populates="department")
