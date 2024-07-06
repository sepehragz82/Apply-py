from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class Professor(Base):
    __tablename__ = "professor"

    professor_id: Mapped[int] = mapped_column(primary_key=True)
    professor_f_name: Mapped[str] = mapped_column(String(200))
    professor_m_name: Mapped[str] = mapped_column(String(200))
    professor_l_name: Mapped[str] = mapped_column(String(200))
    prof_gender: Mapped[bool] = mapped_column(nullable=True)
    prof_code_in_uni: Mapped[int] = mapped_column(nullable=True)
    university_id: Mapped[int] = mapped_column(ForeignKey("university.university_id"))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.department_id"))
    email: Mapped[str] = mapped_column(String(200))
    linkedin: Mapped[str] = mapped_column(String(200), nullable=True)
    google_scholar: Mapped[str] = mapped_column(String(200), nullable=True)
    h_index: Mapped[float] = mapped_column()
    profile_uni_site: Mapped[int] = mapped_column(String(200), nullable=True)
    education_description: Mapped[str] = mapped_column(String(200), nullable=True)
    extra_description: Mapped[str] = mapped_column(String(200), nullable=True)
    academic_rank_id: Mapped[int] = mapped_column(
        ForeignKey("academic_rank.academic_rank_id")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
