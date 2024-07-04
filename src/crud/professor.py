from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ProfessorService:
    def create(self, db: Session, Professor: schemas.ProfessorCreate) -> models.Professor:
        db_item = models.Professor(
            professorFName = Professor.professorFName,
            professorMName = Professor.professorMName,
            professorLName = Professor.professorLName,
            profGender = Professor.profGender,
            profCodeinUni = Professor.profCodeinUni,
            universityID = Professor.universityID,
            departmentID = Professor.departmentID,
            email = Professor.email,
            linkedIN=Professor.linkedIN,
            googleScholar = Professor.googleScholar,
            h_Index = Professor.h_Index,
            profileUniSite = Professor.profileUniSite,
            educationDescription = Professor.educationDescription,
            extraDescription = Professor.extraDescription,
            academicRankID = Professor.academicRankID
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Professor]:
        return (
            db.query(models.Professor)
            .order_by(models.Professor.professorID.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Professor]:
        return (
            db.query(models.Professor)
            .filter(models.Professor.professorID == id)
            .first()
        )

    def update(
        self, db: Session, id: int, item_update: schemas.ProfessorUpdate
    ) -> models.Professor:
        db_item = self.get_by_id(db, id=id)

        update_data = item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.Professor:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


professorService = ProfessorService
