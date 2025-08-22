from fastapi import Depends, FastAPI

from app.api.v1 import api_router
from app.api.v1.deps import get_current_token

app = FastAPI()


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1", dependencies=[Depends(get_current_token)])
