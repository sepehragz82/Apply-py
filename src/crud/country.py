from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class CountryService:
    def create(self, db: Session, country: schemas.CountryCreate) -> models.Country:
        db_item = models.Country(
            countryID = country.countryID,
            countryName = country.countryName
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Country]:
        return (
            db.query(models.Country)
            .order_by(models.Country.countryID())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Country]:
        return db.query(models.Country).filter(models.Country.countryID == id).first()

    def update(
        self, db: Session, id: int, Item_update: schemas.CountryUpdate
    ) -> models.Country:
        db_item = self.get_by_id(db, id=id)

        update_data = Item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.Country:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


countryService = CountryService
