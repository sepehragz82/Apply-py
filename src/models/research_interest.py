from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.session import Base


class ResearchInterest(Base):
    __tablename__ = "research_interest"

    researchInterestID: Mapped[int] = mapped_column(primary_key=True)
    researchInterestName: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    modifiedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
