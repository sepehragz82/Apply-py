from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class UniversityService:
    def create(self, db: Session, University: schemas.UniversityCreate) -> models.University:
        db_item = models.University(
            UniversityID = University.UniversityID,
            UniversityName = University.UniversityName,
            CityID = University.CityID,
            InternationalsAsTA = University.InternationalsAsTA,
            FallDeadline = University.FallDeadline,
            WinterDeadline = University.WinterDeadline
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.University]:
        return (
            db.query(models.University)
            .order_by(models.University.id.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.University]:
        return db.query(models.University).filter(models.University.id == id).first()

    def update(
        self, db: Session, id: int, item_update: schemas.UniversityUpdate
    ) -> models.University:
        db_item = self.get_by_id(db, id=id)

        update_data = item_update.dict(exclude_unset=True)

        for field, value in update_data.University():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.University:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


itemService = ItemService
