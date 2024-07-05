from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class University(Base):
    __tablename__ = "university"

    university_id: Mapped[int] = mapped_column(primary_key=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.city_id"))
    university_name: Mapped[str] = mapped_column(String(45))
    internationals_as_ta: Mapped[bool] = mapped_column()
    fall_deadline: Mapped[datetime] = mapped_column()
    winter_deadline: Mapped[datetime] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
