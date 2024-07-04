from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ItemService:
    def create(self, db: Session, item: schemas.ItemCreate) -> models.Item:
        db_item = models.item(
            name=item.name,
            price=item.price,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Item]:
        return (
            db.query(models.Item)
            .order_by(models.Item.id.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Item]:
        return db.query(models.Item).filter(models.Item.id == id).first()

    def update(
        self, db: Session, id: int, item_update: schemas.ItemUpdate
    ) -> models.Item:
        db_item = self.get_by_id(db, id=id)

        update_data = item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.Item:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


itemService = ItemService
