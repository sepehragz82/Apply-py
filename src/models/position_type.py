from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class PositionType(Base):
    __tablename__ = "position_type"

    position_type_id: Mapped[int] = mapped_column(primary_key=True)
    position_type: Mapped[str] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
