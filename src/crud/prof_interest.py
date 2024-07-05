from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class ProfInterest:
    def create(
        self, db: Session, ProfInterest: schemas.ProfInterestCreate
    ) -> models.ProfInterest:
        db_record = models.ProfInterest(
            professorID=ProfInterest.professor_id,
            researchInterestID=ProfInterest.research_interest_id,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, id: int, data: schemas.ProfInterestUpdate
    ) -> models.ProfInterest:
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

    def delete(self, db: Session, id: int) -> models.ProfInterest:
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.ProfInterest]:
        return (
            db.query(models.ProfInterest)
            .order_by(models.ProfInterest.profResearchInterestID)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.ProfInterest | None:
        return (
            db.query(models.ProfInterest)
            .filter(models.ProfInterest.profResearchInterestID == id)
            .first()
        )


profInterest = ProfInterest()
