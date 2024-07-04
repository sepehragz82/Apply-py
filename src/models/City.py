from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class city(Base):
    __tablename__ = "city"

    CityID = Column(Integer, primary_key=True)
    CityName = Column(String)

    CountryID = relationship("city", back_populates="country")
