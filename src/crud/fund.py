from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class Fund:
    def create(self, db: Session, fund: schemas.FundCreate) -> models.Fund:
        db_fund = models.Fund(
            fundType=fund.fundType,
        )
        db.add(db_fund)
        db.commit()
        db.refresh(db_fund)
        return db_fund

    def update(self, db: Session, id: str, fund: schemas.FundUpdate) -> models.Fund:
        db_fund = self.get_by_id(db, id)

        update_data = fund.dict(exclude_unset=True)
        update_data["modified_at"] = func.now()

        for field, value in update_data.items():
            setattr(db_fund, field, value)

        db.commit()
        db.refresh(db_fund)
        return db_fund

    def delete(self, db: Session, id: int):
        db_fund = self.get_by_id(db, id)
        db.delete(db_fund)
        db.commit()

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> list[models.Fund]:
        return (
            db.query(models.Fund)
            .order_by(models.Fund.id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: id) -> models.Fund | None:
        return db.query(models.Fund).filter(models.Fund.id == id).first()


user = Fund()
