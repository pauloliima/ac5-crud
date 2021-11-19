from sqlalchemy.orm.session import Session
from fastapi import HTTPException
from app.model.table import Item
from app.schema.input import BaseItem, BaseItemUpdate
from app.schema.output import BaseItemOut


def insert(db: Session, item: BaseItem) -> BaseItemOut:
    item = Item(**item.dict())
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error ao inserir o item. {err}")
    return item

def get(db: Session, id: int = None) -> BaseItemOut:
    if id:
        return db.query(Item).filter(Item.id == id).first()
    return db.query(Item).all()

def update(db: Session, id: int, ite: BaseItemUpdate) -> BaseItemOut:
    item = get(id=id, db=db)
    if not item:
        raise HTTPException(
            status_code=400,
            detail="O id informado, não existe.",
        )
    row = ite.dict(exclude_none=True)
    if not row: 
        raise HTTPException(
            status_code=400,
            detail="Não existe dados para ser atualizados.",
        )
    db.query(Item).filter(Item.id == id).update(
        row, synchronize_session=False
    )
    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, id: int) -> BaseItemOut:
    item = get(id=id, db=db)
    if not item:
        raise HTTPException(
            status_code=400,
            detail="O id informado, não existe.",
        )
    data = BaseItemOut.from_orm(item)
    db.delete(item)
    db.commit()
    return data