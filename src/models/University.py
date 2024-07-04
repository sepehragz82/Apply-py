from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class University(Base):
    __tablename__ = "university"

    universityID = Column(Integer, primary_key=True)
    universityName = Column(String)
    internationalsAsTA = Column(Boolean)
    fallDeadline = Column(DateTime)
    winterDeadline = Column(DateTime)

    cityID = relationship("university", back_populates="city")
