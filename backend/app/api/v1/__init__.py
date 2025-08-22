from fastapi import APIRouter

from .routers import items, locations, stock

api_router = APIRouter()
api_router.include_router(items.router)
api_router.include_router(locations.router)
api_router.include_router(stock.router)
