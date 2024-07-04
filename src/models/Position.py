from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class position(Base):
    __tablename__ = "position"

    PositionID = Column(Integer, primary_key=True)
    PossisionOn = Column(Boolean)
    PositionYear = Column(Integer)

    ProfessorID = relationship("position", back_populates="professor")
    FundID = relationship("position", back_populates="fund")
    PositionTypeID = relationship("position", back_populates="position_type")
    DepartmentID = relationship("position", back_populates="department")
