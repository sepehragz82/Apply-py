from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class Fund:
    def create(self, db: Session, fund: schemas.FundCreate) -> models.Fund:
        db_record = models.Fund(
            fund_type=fund.fund_type,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(self, db: Session, id: int, data: schemas.FundUpdate) -> models.Fund:
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

    def delete(self, db: Session, id: int):
        db_record = self.get_by_id(db, id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Fund]:
        return (
            db.query(models.Fund)
            .order_by(models.Fund.fund_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.Fund | None:
        return db.query(models.Fund).filter(models.Fund.fund_id == id).first()


fund = Fund()
