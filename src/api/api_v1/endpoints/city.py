from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.City)
def create(
    data: schemas.CityCreate,
    db: Session = Depends(deps.get_db),
):
    return crud.city.create(db, data)


@router.put("/{id}", response_model=schemas.City)
def update(
    id: int,
    data: schemas.CityUpdate,
    db: Session = Depends(deps.get_db),
):
    return crud.city.update(db, id, data)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(deps.get_db),
):
    crud.city.delete(db, id)


@router.get("/all/", response_model=list[schemas.City])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return crud.city.get_all(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=schemas.City)
def get_by_id(
    id: int,
    db: Session = Depends(deps.get_db),
):
    db_record = crud.city.get_by_id(db, id=id)

    if db_record is None:
        raise HTTPException(status_code=404, detail="Record not found")

    return db_record
