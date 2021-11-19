from datetime import datetime
from pydantic import validator
from app.schema.input import BaseItem


class BaseItemOut(BaseItem):
    id: int
    created_at: datetime
    updated_at: datetime
    active: bool

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"
