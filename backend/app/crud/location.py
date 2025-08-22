from sqlalchemy.orm import Session

from app import models, schemas


def get(db: Session, location_id: int) -> models.Location | None:
    return db.get(models.Location, location_id)


def get_multi(db: Session, skip: int = 0, limit: int = 100) -> list[models.Location]:
    return db.query(models.Location).offset(skip).limit(limit).all()


def create(db: Session, obj_in: schemas.LocationCreate) -> models.Location:
    db_obj = models.Location(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update(
    db: Session, db_obj: models.Location, obj_in: schemas.LocationUpdate
) -> models.Location:
    for field, value in obj_in.model_dump().items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def remove(db: Session, db_obj: models.Location) -> models.Location:
    db.delete(db_obj)
    db.commit()
    return db_obj
