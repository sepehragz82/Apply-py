from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class University:
    def create(self, db: Session, data: schemas.UniversityCreate) -> models.University:
        db_record = models.University(
            city_id=data.city_id,
            university_name=data.university_name,
            internationals_as_ta=data.internationals_as_ta,
            fall_deadline=data.fall_deadline,
            winter_deadline=data.winter_deadline,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, id: int, data: schemas.UniversityUpdate
    ) -> models.University:
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

    def delete(self, db: Session, id: int) -> models.University:
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.University]:
        return (
            db.query(models.University)
            .order_by(models.University.university_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.University | None:
        return (
            db.query(models.University)
            .filter(models.University.university_id == id)
            .first()
        )


university = University()
