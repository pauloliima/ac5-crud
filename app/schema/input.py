from pydantic import BaseModel


class BaseItem(BaseModel):
    name: str
    qty: int
    price: float
    active: bool = True

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseItemUpdate(BaseModel):
    name: str = None
    qty: int = None
    price: float = None
    active: bool = None
