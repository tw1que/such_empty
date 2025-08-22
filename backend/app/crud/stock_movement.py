from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app import models, schemas


def create(db: Session, obj_in: schemas.StockMovementCreate) -> models.StockMovement:
    db_obj = models.StockMovement(**obj_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_multi(
    db: Session, item_id: int | None = None, location_id: int | None = None
) -> list[models.StockMovement]:
    query = db.query(models.StockMovement)
    if item_id is not None:
        query = query.filter(models.StockMovement.item_id == item_id)
    if location_id is not None:
        query = query.filter(models.StockMovement.location_id == location_id)
    return query.all()


def stock_levels(
    db: Session, item_id: int | None = None, location_id: int | None = None
) -> list[dict[str, int]]:
    stmt = (
        select(
            models.StockMovement.item_id,
            models.StockMovement.location_id,
            func.sum(models.StockMovement.delta_qty).label("qty"),
        )
        .group_by(models.StockMovement.item_id, models.StockMovement.location_id)
    )
    if item_id is not None:
        stmt = stmt.where(models.StockMovement.item_id == item_id)
    if location_id is not None:
        stmt = stmt.where(models.StockMovement.location_id == location_id)
    result = db.execute(stmt).all()
    return [
        {"item_id": r.item_id, "location_id": r.location_id, "qty": r.qty}
        for r in result
    ]
