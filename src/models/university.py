from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class University(Base):
    __tablename__ = "university"

    universityID: Mapped[int] = mapped_column(primary_key=True)
    cityID: Mapped[int] = mapped_column(ForeignKey("city.id"))
    universityName: Mapped[str] = mapped_column()
    internationalsAsTA: Mapped[bool] = mapped_column()
    fallDeadline: Mapped[datetime] = mapped_column()
    winterDeadline: Mapped[datetime] = mapped_column()

    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modifiedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
