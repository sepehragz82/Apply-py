from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class PositionType(Base):
    __tablename__ = "position_type"

    positionTypeID: Mapped[int] = mapped_column(primary_key=True)
    positionType: Mapped[str] = mapped_column()

    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modifiedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
