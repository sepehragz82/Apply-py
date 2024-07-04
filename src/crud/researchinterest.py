from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ResearchInterestService:
    def create(self, db: Session, ResearchInterest: schemas.ResearchInterestCreate) -> models.ResearchInterest:
        db_item = models.ResearchInterest(
            researchInterestID = ResearchInterest.researchInterestID,
            researchInterestName = ResearchInterest.researchInterestName,
            description = ResearchInterest.description
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.ResearchInterest]:
        return (
            db.query(models.ResearchInterest)
            .order_by(models.ResearchInterest.researchInterestID())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.ResearchInterest]:
        return db.query(models.ResearchInterest).filter(models.ResearchInterest.researchInterestID == id).first()

    def update(
        self, db: Session, id: int, Item_update: schemas.ResearchInterestUpdate
    ) -> models.ResearchInterest:
        db_item = self.get_by_id(db, id=id)

        update_data = Item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.ResearchInterest:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


researchInterestService = ResearchInterestService
