from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class ProfessorService:
    def create(self, db: Session, Professor: schemas.ProfessorCreate) -> models.Item:
        db_item = models.Item(
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
            db.query(models.Item)
            .order_by(models.Item.id.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Professor]:
        return db.query(model

        s.Professor).filter(models.Professor.id == id).first()

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
