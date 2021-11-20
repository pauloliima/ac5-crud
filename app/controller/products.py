from sqlalchemy.orm.session import Session
from fastapi import HTTPException
from app.model.table import Product
from app.schema.input import BaseProduct, BaseProductUpdate
from app.schema.output import BaseProductOut


def insert(db: Session, product: BaseProduct) -> BaseProductOut:
    product = Product(**product.dict())
    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error ao inserir o product. {err}")
    return product

def get(db: Session, id: int = None) -> BaseProductOut:
    if id:
        return db.query(Product).filter(Product.id == id).first()
    return db.query(Product).all()

def update(db: Session, id: int, ite: BaseProductUpdate) -> BaseProductOut:
    product = get(id=id, db=db)
    if not product:
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
    db.query(Product).filter(Product.id == id).update(
        row, synchronize_session=False
    )
    db.commit()
    db.refresh(product)
    return product

def delete(db: Session, id: int) -> BaseProductOut:
    product = get(id=id, db=db)
    if not product:
        raise HTTPException(
            status_code=400,
            detail="O id informado, não existe.",
        )
    data = BaseProductOut.from_orm(product)
    db.delete(product)
    db.commit()
    return data