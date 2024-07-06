from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class ResearchInterest(Base):
    __tablename__ = "research_interest"

    research_interest_id: Mapped[int] = mapped_column(primary_key=True)
    research_interest_name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(200))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
