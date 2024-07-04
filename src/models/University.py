from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from src.database.session import Base


class university(Base):
    __tablename__ = "university"

    UnivercityID = Column(Integer, primary_key=True, index=True)
    UniversityName = Column(String, index=True)
    InternationalsAsTA = Column(Boolean, index=True)
    FallDeadline = Column(DateTime, index=True)
    WinterDeadline = Column(DateTime, index=True)

    CityID = relationship("university", back_populates="city")
