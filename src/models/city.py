from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class City(Base):
    __tablename__ = "city"

    cityID: Mapped[int] = mapped_column(primary_key=True)
    cityName: Mapped[str] = mapped_column()
    countryID: Mapped[int] = mapped_column(ForeignKey("country.countryID"))

    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modifiedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
