from typing import List
from fastapi import APIRouter, FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.controller import item
from app.model.database import get_db
from app.schema.input import BaseItem, BaseItemUpdate
from app.schema.output import BaseItemOut
from app.schema.erro import Error400


def init_app(app: FastAPI):
    router = APIRouter(tags=["Item"])
    error_400 = {400: {"model": Error400, "description": "id invalido."}}

    @router.get("/item", response_model=List[BaseItemOut])
    async def get_item(db: session = Depends(get_db)):
        return item.get(db=db)

    @router.get("/item/{id}", response_model=BaseItemOut)
    async def get_item_by_id(id: int = None, db: session = Depends(get_db)):
        return item.get(id=id, db=db)

    @router.post("/item", response_model=BaseItemOut, responses=error_400)
    async def post_item(data: BaseItem, db: session = Depends(get_db)):
        return item.insert(item=data, db=db)

    @router.patch("/item/{id}", response_model=BaseItemOut, responses=error_400)
    async def patch_item(id: int, data: BaseItemUpdate, db: session = Depends(get_db)):
        return item.update(id=id, ite=data, db=db)

    @router.delete("/item/{id}", response_model=BaseItemOut, responses=error_400)
    async def delete_item(id: int, db: session = Depends(get_db)):
        return item.delete(id=id, db=db)

    app.include_router(router=router)
