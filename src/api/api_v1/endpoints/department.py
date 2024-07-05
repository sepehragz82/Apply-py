from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Department)
def create(
    data: schemas.DepartmentCreate,
    db: Session = Depends(deps.get_db),
):
    return crud.department.create(db, data)


@router.put("/{id}", response_model=schemas.Department)
def update(
    id: int,
    data: schemas.DepartmentUpdate,
    db: Session = Depends(deps.get_db),
):
    return crud.department.update(db, id, data)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(deps.get_db),
):
    crud.department.delete(db, id)


@router.get("/all/", response_model=list[schemas.Department])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return crud.department.get_all(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=schemas.Department)
def get_by_id(
    id: int,
    db: Session = Depends(deps.get_db),
):
    db_record = crud.department.get_by_id(db, id=id)

    if db_record is None:
        raise HTTPException(status_code=404, detail="Record not found")

    return db_record
