from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ProfessorService:
    def create(self, db: Session, Professor: schemas.ProfessorCreate) -> models.Professor:
        db_item = models.Professor(
            ProfessorID = Professor.ProfessorID,
            ProfessorFName = Professor.ProfessorFName,
            ProfessorMName = Professor.ProfessorMName,
            ProfessorLName = Professor.ProfessorLName,
            ProfGender = Professor.ProfGender,
            ProfCodeinUni = Professor.ProfCodeinUni,
            UniversityID = Professor.UniversityID,
            DepartmentID = Professor.DepartmentID,
            Email = Professor.Email,
            LinkedIN = Professor.LinkedIN,
            GoogleScholar = Professor.GoogleScholar,
            H_Index = Professor.H_Index,
            ProfileUniSite = Professor.ProfileUniSite,
            EducationDescription = Professor.EducationDescription,
            ExtraDescription = Professor.ExtraDescription,
            AcademicRankID = Professor.AcademicRankID
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
            .order_by(models.Professor.ProfessorID.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Professor]:
        return db.query(models.Professor).filter(models.Professor.professorID == id).first()

    def update(
        self, db: Session, id: int, item_update: schemas.ProfessorUpdate) -> models.Professor:
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


ProfessorService = ProfessorService
