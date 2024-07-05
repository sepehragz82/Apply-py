from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class Position:
    def create(self, db: Session, Position: schemas.PositionCreate) -> models.Position:
        db_record = models.Position(
            fund_id=Position.fund_id,
            position_on=Position.position_on,
            professor_id=Position.professor_id,
            department_id=Position.department_id,
            position_type_id=Position.position_type_id,
            position_year=Position.position_year,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, id: int, data: schemas.PositionUpdate
    ) -> models.Position:
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

    def delete(self, db: Session, id: int) -> models.Position:
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Position]:
        return (
            db.query(models.Position)
            .order_by(models.Position.position_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.Position | None:
        return (
            db.query(models.Position).filter(models.Position.position_id == id).first()
        )


position = Position()
