from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    sku: str
    name: str
    description: str | None = None
    min_qty: int = 0
    is_active: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
