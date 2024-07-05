from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from src import models, schemas


class Professor:
    def create(self, db: Session, data: schemas.ProfessorCreate) -> models.Professor:
        db_record = models.Professor(
            professor_f_name=data.professor_f_name,
            professor_m_name=data.professor_m_name,
            professor_l_name=data.professor_l_name,
            prof_gender=data.prof_gender,
            prof_code_in_uni=data.prof_code_in_uni,
            university_id=data.university_id,
            department_id=data.department_id,
            email=data.email,
            linkedin=data.linkedin,
            google_scholar=data.google_scholar,
            h_index=data.h_index,
            profile_uni_site=data.profile_uni_site,
            education_description=data.education_description,
            extra_description=data.extra_description,
            academic_rank_id=data.academic_rank_id,
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
        db_record = self.get_by_id(db, id)

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
            .order_by(models.Professor.professor_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> models.Professor | None:
        return (
            db.query(models.Professor)
            .filter(models.Professor.professor_id == id)
            .first()
        )


professor = Professor()
