from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LocationBase(BaseModel):
    code: str
    name: str


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
