from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.session import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(float, index=True)

    author_id = relationship("User", back_populates="notes")
 
    """
        user_preference = Table(
        "user_preference",
        metadata_obj,
        Column("pref_id", Integer, primary_key=True),
        Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
        Column("pref_name", String(40), nullable=False),
        Column("pref_value", String(100)),
        )
    """