from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class PositionService:
    def create(self, db: Session, Position: schemas.PositionCreate) -> models.Position:
        db_item = models.Position(
            positionOn=Position.position_on,
            positionYear=Position.position_year,
            professorID=Position.professor_id,
            fundID=Position.fund_id,
            positionTypeID=Position.position_type_id,
            departmentID=Position.department_id,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Position]:
        return (
            db.query(models.Position)
            .order_by(models.Position.positionID())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Position]:
        return (
            db.query(models.Position).filter(models.Position.positionID == id).first()
        )

    def update(
        self, db: Session, id: int, Item_update: schemas.PositionUpdate
    ) -> models.Position:
        db_item = self.get_by_id(db, id=id)

        update_data = Item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.Position:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


positionService = PositionService
