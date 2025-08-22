from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StockMovementBase(BaseModel):
    item_id: int
    location_id: int
    delta_qty: int
    reason: str | None = None


class StockMovementCreate(StockMovementBase):
    pass


class StockMovementRead(StockMovementBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
