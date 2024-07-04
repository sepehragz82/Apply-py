from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from src.database.session import Base


class position(Base):
    __tablename__ = "position"

    PositionID = Column(Integer, primary_key=True, index=True)
    FundID = Column(ForeignKey, index=True)
    PossisionOn = Column(Boolean, index=True)
    DepartmentID = Column(ForeignKey, index=True)
    PositionTypeID = Column(ForeignKey, index=True)
    PositionYear = Column(Integer, index=True)

    author_id = relationship("User", back_populates="notes")
