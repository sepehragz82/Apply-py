from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class PositionTypeService:
    def create(self, db: Session, Position: schemas.PositionCreate) -> models.PositionType:
        db_item = models.PositionType(
            positionType = PositionType.positionType
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.PositionType]:
        return (
            db.query(models.PositionType)
            .order_by(models.PositionType.positionID())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.PositionType]:
        return db.query(models.PositionType).filter(models.PositionType.positionID == id).first()

    def update(
        self, db: Session, id: int, Item_update: schemas.PositionUpdate
    ) -> models.PositionType:
        db_item = self.get_by_id(db, id=id)

        update_data = Item_update.dict(exclude_unset=True)

        for field, value in update_data.PositionType():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.PositionType:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


positionTypeService = PositionTypeService
