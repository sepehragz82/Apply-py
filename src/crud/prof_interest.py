from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ProfInterestService:
    def create(
        self, db: Session, ProfInterest: schemas.ProfInterestCreate
    ) -> models.ProfInterest:
        db_item = models.ProfInterest(
            profInterest=ProfInterest.profInterest,
            professorID=ProfInterest.professor_id,
            researchInterestID=ProfInterest.research_interest_id,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.ProfInterest]:
        return (
            db.query(models.ProfInterest)
            .order_by(models.ProfInterest.profInterestID())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.ProfInterest]:
        return (
            db.query(models.ProfInterest)
            .filter(models.ProfInterest.profInterestID == id)
            .first()
        )

    def update(
        self, db: Session, id: int, Item_update: schemas.ProfInterestUpdate
    ) -> models.ProfInterest:
        db_item = self.get_by_id(db, id=id)

        update_data = Item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.ProfInterest:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


profInterestService = ProfInterestService
