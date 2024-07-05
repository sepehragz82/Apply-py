from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class Position(Base):
    __tablename__ = "position"

    position_id: Mapped[int] = mapped_column(primary_key=True)
    fund_id: Mapped[int] = mapped_column(ForeignKey("fund.fund_id"))
    position_on: Mapped[bool] = mapped_column()
    professor_id: Mapped[int] = mapped_column(ForeignKey("professor.professor_id"))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.department_id"))
    position_type_id: Mapped[int] = mapped_column(
        ForeignKey("position_type.position_type_id")
    )
    position_year: Mapped[int] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
