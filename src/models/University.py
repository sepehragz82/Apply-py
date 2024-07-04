from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class university(Base):
    __tablename__ = "university"

    UnivercityID = Column(Integer, primary_key=True)
    UniversityName = Column(String)
    InternationalsAsTA = Column(Boolean)
    FallDeadline = Column(DateTime)
    WinterDeadline = Column(DateTime)

    CityID = relationship("university", back_populates="city")
