from typing import List, Optional

from sqlalchemy.orm import Session

from src import models, schemas


class DepartmentService:
    def create(
        self, db: Session, department: schemas.DepartmentCreate
    ) -> models.Department:
        db_item = models.Department(
            departmentID=department.departmentID,
            departmentName=department.department_name,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_all(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.Department]:
        return (
            db.query(models.Department)
            .order_by(models.Department.departmentID.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, db: Session, id: int) -> Optional[models.Department]:
        return (
            db.query(models.Department)
            .filter(models.Department.departmentID == id)
            .first()
        )

    def update(
        self, db: Session, id: int, item_update: schemas.Department
    ) -> models.Department:
        db_item = self.get_by_id(db, id=id)

        update_data = item_update.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_item, field, value)

        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, id: int) -> models.Department:
        db_item = self.get_by_id(db, id=id)
        db.delete(db_item)
        db.commit()
        return db_item


DepartmentService = DepartmentService
