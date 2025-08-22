from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.v1 import deps

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[schemas.ItemRead])
def list_items(db: Session = Depends(deps.get_db)):
    return crud.item.get_multi(db)


@router.post("/", response_model=schemas.ItemRead)
def create_item(item_in: schemas.ItemCreate, db: Session = Depends(deps.get_db)):
    return crud.item.create(db, item_in)


@router.get("/{item_id}", response_model=schemas.ItemRead)
def get_item(item_id: int, db: Session = Depends(deps.get_db)):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=schemas.ItemRead)
def update_item(
    item_id: int, item_in: schemas.ItemUpdate, db: Session = Depends(deps.get_db)
):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.item.update(db, item, item_in)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(deps.get_db)):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud.item.remove(db, item)
    return {"ok": True}
