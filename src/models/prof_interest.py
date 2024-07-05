from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class ProfInterest(Base):
    __tablename__ = "prof_interest"

    profResearchInterestID: Mapped[int] = mapped_column(primary_key=True)
    professorID: Mapped[int] = mapped_column(ForeignKey("professor.professorID"))
    research_interest_id: Mapped[int] = mapped_column(
        ForeignKey("research_interest.research_interest_id")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
