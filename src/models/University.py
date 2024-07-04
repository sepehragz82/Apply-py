from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from src.database.session import Base


class university(Base):
    __tablename__ = "university"

    UniversityName = Column(String, primary_key=True, index=True)
    CityID = Column(Integer, index=True)
    InternationalsAsTA = Column(Boolean, index=True)
    FallDeadline = Column(DateTime, index=True)
    WinterDeadline = Column(DateTime, index=True)

    author_id = relationship("User", back_populates="notes")
