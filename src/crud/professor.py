from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class Professor:
    def create(self, db: Session, data: schemas.ProfessorCreate) -> models.Professor:
        db_record = models.Professor(
            professorFName=data.professor_f_name,
            professorMName=data.professor_m_name,
            professorLName=data.professor_l_name,
            profGender=data.prof_gender,
            profCodeinUni=data.prof_code_in_uni,
            universityID=data.university_id,
            departmentID=data.department_id,
            email=data.email,
            linkedIN=data.linkedin,
            googleScholar=data.google_scholar,
            h_Index=data.h_index,
            profileUniSite=data.profile_uni_site,
            educationDescription=data.education_description,
            extraDescription=data.extra_description,
            academicRankID=data.academic_rank_id,
        )
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record

    def update(
        self, db: Session, id: int, data: schemas.ProfessorUpdate
    ) -> models.Professor:
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

    def delete(self, db: Session, id: int) -> models.Professor:
        db_record = self.get_by_id(db, id=id)

        if db_record is None:
            raise HTTPException(status_code=404, detail="Record not found")

        db.delete(db_record)
        db.commit()
        return db_record

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Professor]:
        return (
            db.query(models.Professor)
            .order_by(models.Professor.professorID)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.Professor | None:
        return (
            db.query(models.Professor)
            .filter(models.Professor.professorID == id)
            .first()
        )


professor = Professor()
