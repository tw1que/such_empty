from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.v1 import deps

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("/", response_model=list[schemas.LocationRead])
def list_locations(db: Session = Depends(deps.get_db)):
    return crud.location.get_multi(db)


@router.post("/", response_model=schemas.LocationRead)
def create_location(
    location_in: schemas.LocationCreate, db: Session = Depends(deps.get_db)
):
    return crud.location.create(db, location_in)


@router.get("/{location_id}", response_model=schemas.LocationRead)
def get_location(location_id: int, db: Session = Depends(deps.get_db)):
    loc = crud.location.get(db, location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc


@router.put("/{location_id}", response_model=schemas.LocationRead)
def update_location(
    location_id: int,
    location_in: schemas.LocationUpdate,
    db: Session = Depends(deps.get_db),
):
    loc = crud.location.get(db, location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return crud.location.update(db, loc, location_in)


@router.delete("/{location_id}")
def delete_location(location_id: int, db: Session = Depends(deps.get_db)):
    loc = crud.location.get(db, location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    crud.location.remove(db, loc)
    return {"ok": True}
