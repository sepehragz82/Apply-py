from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class City(Base):
    __tablename__ = "city"

    cityID = Column(Integer, primary_key=True)
    cityName = Column(String)

    countryID = relationship("city", back_populates="country")
