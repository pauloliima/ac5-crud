from typing import List
from fastapi import APIRouter, FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.controller import products
from app.model.database import get_db
from app.schema.input import BaseProduct, BaseProductUpdate
from app.schema.output import BaseProductOut
from app.schema.erro import Error400


def init_app(app: FastAPI):
    router = APIRouter(tags=["Product"])
    error_400 = {400: {"model": Error400, "description": "id invalido."}}

    @router.get("/products", response_model=List[BaseProductOut])
    async def get_products(db: session = Depends(get_db)):
        return products.get(db=db)

    @router.get("/products/{id}", response_model=BaseProductOut)
    async def get_products_by_id(id: int = None, db: session = Depends(get_db)):
        return products.get(id=id, db=db)

    @router.post("/products", response_model=BaseProductOut, responses=error_400)
    async def post_products(data: BaseProduct, db: session = Depends(get_db)):
        return products.insert(product=data, db=db)

    @router.patch("/products/{id}", response_model=BaseProductOut, responses=error_400)
    async def patch_products(id: int, data: BaseProductUpdate, db: session = Depends(get_db)):
        return products.update(id=id, ite=data, db=db)

    @router.delete("/products/{id}", response_model=BaseProductOut, responses=error_400)
    async def delete_products(id: int, db: session = Depends(get_db)):
        return products.delete(id=id, db=db)

    app.include_router(router=router)
