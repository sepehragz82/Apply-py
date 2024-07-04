from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class AcademicRank:
    def create(
        self, db: Session, academic_rank: schemas.AcademicRankCreate
    ) -> models.AcademicRank:
        db_academic_rank = models.AcademicRank(
            academicRankTitle=academic_rank.academicRankTitle,
        )
        db.add(db_academic_rank)
        db.commit()
        db.refresh(db_academic_rank)
        return db_academic_rank

    def update(
        self, db: Session, id: str, academic_rank: schemas.AcademicRankUpdate
    ) -> models.AcademicRank:
        db_academic_rank = self.get_by_id(db, id)

        update_data = academic_rank.dict(exclude_unset=True)
        update_data["modified_at"] = func.now()

        for field, value in update_data.items():
            setattr(db_academic_rank, field, value)

        db.commit()
        db.refresh(db_academic_rank)
        return db_academic_rank

    def delete(self, db: Session, id: int):
        db_academic_rank = self.get_by_id(db, id)
        db.delete(db_academic_rank)
        db.commit()

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> list[models.AcademicRank]:
        return (
            db.query(models.AcademicRank)
            .order_by(models.AcademicRank.id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: id) -> models.AcademicRank | None:
        return (
            db.query(models.AcademicRank).filter(models.AcademicRank.id == id).first()
        )


user = AcademicRank()
