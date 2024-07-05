from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas
from src.core.security import get_password_hash, verify_password


class User:
    def create(self, db: Session, data: schemas.UserCreate) -> models.User:
        db_record = models.User(
            username=data.username,
            hashed_password=get_password_hash(data.password),
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, username: str, data: schemas.UserUpdate
    ) -> models.User:
        db_record = self.get_user_by_username(db, username=username)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        update_data = data.model_dump(exclude_unset=True)
        update_data["modified_at"] = func.now()

        for field, value in update_data.items():
            setattr(db_record, field, value)

        db.commit()
        db.refresh(db_record)
        return db_record

    def delete(self, db: Session, username: str) -> models.User:
        db_record = self.get_user_by_username(db, username=username)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def update_password(
        self, db: Session, username: str, new_password: str
    ) -> models.User:
        db_record = self.get_user_by_username(db, username=username)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        hashed_password = get_password_hash(new_password)
        setattr(db_record, "hashed_password", hashed_password)
        setattr(db_record, "modified_at", func.now())

        db.commit()
        db.refresh(db_record)
        return db_record

    def authenticate(
        self, db: Session, username: str, password: str
    ) -> models.User | None:
        db_record = self.get_user_by_username(db, username=username)

        if not db_record:
            return None

        if not verify_password(password, db_record.hashed_password):
            return None

        return db_record

    def get_all_users(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.User]:
        return (
            db.query(models.User)
            .order_by(models.User.id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_user_by_id(self, db: Session, id: int) -> models.User | None:
        return db.query(models.User).filter(models.User.id == id).first()

    def get_user_by_username(self, db: Session, username: str) -> models.User | None:
        return db.query(models.User).filter(models.User.username == username).first()


user = User()
