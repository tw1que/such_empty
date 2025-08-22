from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from .item import Item  # noqa: E402
from .location import Location  # noqa: E402
from .stock_movement import StockMovement  # noqa: E402


__all__ = ["Base", "Item", "Location", "StockMovement"]
