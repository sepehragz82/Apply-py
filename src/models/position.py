from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class Position(Base):
    __tablename__ = "position"

    positionID: Mapped[int] = mapped_column(primary_key=True)
    fundID: Mapped[int] = mapped_column(ForeignKey("fund.fundID"))
    positionOn: Mapped[bool] = mapped_column()
    professorID: Mapped[int] = mapped_column(ForeignKey("professor.professorID"))
    departmentID: Mapped[int] = mapped_column(ForeignKey("department.departmentID"))
    positionTypeID: Mapped[int] = mapped_column(
        ForeignKey("position_type.positionTypeID")
    )
    positionYear: Mapped[int] = mapped_column()

    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modifiedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
