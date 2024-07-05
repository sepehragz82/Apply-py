from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class PositionType:
    def create(
        self, db: Session, data: schemas.PositionTypeCreate
    ) -> models.PositionType:
        db_record = models.PositionType(position_type=data.position_type)
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, id: int, data: schemas.PositionTypeUpdate
    ) -> models.PositionType:
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        update_data = data.model_dump(exclude_unset=True)
        update_data["modified_at"] = func.now()

        for field, value in update_data.items():
            setattr(db_record, field, value)

        db.commit()
        db.refresh(db_record)
        return db_record

    def delete(self, db: Session, id: int) -> models.PositionType:
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.PositionType]:
        return (
            db.query(models.PositionType)
            .order_by(models.PositionType.position_type_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.PositionType | None:
        return (
            db.query(models.PositionType)
            .filter(models.PositionType.position_type_id == id)
            .first()
        )


position_type = PositionType()
