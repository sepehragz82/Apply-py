from sqlalchemy.orm import Session

from src import crud, models
from src.core.config import settings
from src.core.security import get_password_hash
from src.database import base  # keep


def init_db(db: Session):
    pass
