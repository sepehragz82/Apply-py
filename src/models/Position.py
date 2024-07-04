from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from src.database.session import Base


class position(Base):
    __tablename__ = "position"

    PositionID = Column(Integer, primary_key=True, index=True)
    PossisionOn = Column(Boolean, index=True)
    PositionYear = Column(Integer, index=True)

    ProfessorID = relationship("position", back_populates="professor")
    FundID = relationship("position", back_populates="fund")
    PositionTypeID = relationship("position", back_populates="position_type")
    DepartmentID = relationship("position", back_populates="department")
