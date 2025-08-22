from sqlalchemy.orm import Session

from app import models, schemas


def get(db: Session, item_id: int) -> models.Item | None:
    return db.get(models.Item, item_id)


def get_multi(db: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def create(db: Session, obj_in: schemas.ItemCreate) -> models.Item:
    db_obj = models.Item(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update(db: Session, db_obj: models.Item, obj_in: schemas.ItemUpdate) -> models.Item:
    for field, value in obj_in.model_dump().items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def remove(db: Session, db_obj: models.Item) -> models.Item:
    db.delete(db_obj)
    db.commit()
    return db_obj
