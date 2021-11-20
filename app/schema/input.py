from pydantic import BaseModel


class BaseProduct(BaseModel):
    name: str
    qty: int
    price: float
    active: bool = True

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseProductUpdate(BaseModel):
    name: str = None
    qty: int = None
    price: float = None
    active: bool = None
