from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from src.database.session import Base


class Country(Base):
    __tablename__ = "country"

    CountryID = Column(Integer, primary_key=True, index=True)
    CountryName = Column(String, index=True)
