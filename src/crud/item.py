from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ItemManager(object):
    def __init__(self):
        pass

    def create(self, db: Session, user: schemas.Item) -> models.Item:
        db_item = models.Item(
            name=user.name,
            price=user.price,
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
            .filter(models.Item.public == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Item]:
        return db.query(models.Item).filter(models.Item.id == id).first()

    def update(
        self, db: Session, id: int, item_update: schemas.ItemUpdate
    ) -> models.Item:
        db_note = self.get_by_id(db, id=id)

        update_data = item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_note, field, value)

        db.commit()
        db.refresh(db_note)
        return db_note

    def remove(self, db: Session, id: int) -> models.Note:
        db_note = self.get_by_id(db, id=id)
        db.delete(db_note)
        db.commit()
        return db_note
