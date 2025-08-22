from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.v1 import deps

router = APIRouter(prefix="/stock", tags=["stock"])


@router.get("/levels")
def stock_levels(
    item_id: int | None = None,
    location_id: int | None = None,
    db: Session = Depends(deps.get_db),
):
    return crud.stock_movement.stock_levels(db, item_id=item_id, location_id=location_id)


@router.post("/movements", response_model=schemas.StockMovementRead)
def create_movement(
    movement_in: schemas.StockMovementCreate, db: Session = Depends(deps.get_db)
):
    return crud.stock_movement.create(db, movement_in)


@router.get("/movements", response_model=list[schemas.StockMovementRead])
def list_movements(
    item_id: int | None = None,
    location_id: int | None = None,
    db: Session = Depends(deps.get_db),
):
    return crud.stock_movement.get_multi(
        db, item_id=item_id, location_id=location_id
    )
