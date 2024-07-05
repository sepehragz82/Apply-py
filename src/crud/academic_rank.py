from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class AcademicRank:
    def create(
        self, db: Session, data: schemas.AcademicRankCreate
    ) -> models.AcademicRank:
        db_record = models.AcademicRank(
            academicRankTitle=data.academic_rank_title,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, id: int, data: schemas.AcademicRankUpdate
    ) -> models.AcademicRank:
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

    def delete(self, db: Session, id: int) -> models.AcademicRank:
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.AcademicRank]:
        return (
            db.query(models.AcademicRank)
            .order_by(models.AcademicRank.academicRankID)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.AcademicRank | None:
        return (
            db.query(models.AcademicRank)
            .filter(models.AcademicRank.academicRankID == id)
            .first()
        )


academic_rank = AcademicRank()
