from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.database.session import Base


class city(Base):
    __tablename__ = "city"

    CityID = Column(Integer, primary_key=True, index=True)
    CityName = Column(String, index=True)
    CountryID = Column(ForeignKey, index=True)

    author_id = relationship("User", back_populates="notes")