from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return crud.ItemManager.get_all(db, skip=skip, limit=limit)


@router.get("/id", response_model=schemas.Item)
def get_by_id(
    id: int,
    db: Session = Depends(deps.get_db),
):
    db_item = crud.ItemManager.get_by_id(db, id=id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item


@router.post("/", response_model=schemas.Item)
def create(
    item: schemas.ItemCreate,
    db: Session = Depends(deps.get_db),
):
    return crud.ItemManager.create(db, item=item)


@router.put("/", response_model=schemas.Item)
def update(
    id: int,
    item_update: schemas.ItemUpdate,
    db: Session = Depends(deps.get_db),
):
    db_item = crud.ItemManager.get_by_id(db, id=id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return crud.ItemManager.update(db, id=id, item_update=item_update)


@router.delete("/", response_model=schemas.Item)
def delete(
    id: int,
    db: Session = Depends(deps.get_db),
):
    db_item = crud.ItemManager.get_by_id(db, id=id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return crud.ItemManager.delete(db, id=id)
