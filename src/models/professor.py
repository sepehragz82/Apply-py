from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class Professor(Base):
    __tablename__ = "professor"

    professorID: Mapped[int] = mapped_column(primary_key=True)
    professorFName: Mapped[str] = mapped_column()
    professorMName: Mapped[str] = mapped_column()
    professorLName: Mapped[str] = mapped_column()
    profGender: Mapped[bool] = mapped_column(nullable=True)
    profCodeinUni: Mapped[int] = mapped_column(nullable=True)
    universityID: Mapped[int] = mapped_column(ForeignKey("university.universityID"))
    departmentID: Mapped[int] = mapped_column(ForeignKey("department.departmentID"))
    email: Mapped[str] = mapped_column()
    linkedIN: Mapped[str] = mapped_column(nullable=True)
    googleScholar: Mapped[str] = mapped_column(nullable=True)
    h_Index: Mapped[float] = mapped_column()
    profileUniSite: Mapped[int] = mapped_column(nullable=True)
    educationDescription: Mapped[str] = mapped_column(nullable=True)
    extraDescription: Mapped[str] = mapped_column(nullable=True)
    academicRankID: Mapped[int] = mapped_column(
        ForeignKey("academic_rank.academicRankID")
    )

    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modifiedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
