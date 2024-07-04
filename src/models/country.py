from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from src.database.session import Base


class Country(Base):
    __tablename__ = "country"

    countryID = Column(Integer, primary_key=True)
    countryName = Column(String)
