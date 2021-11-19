from datetime import datetime
import sqlalchemy
from app.config.config import settings
from app.model.database import Base


class Item(Base):
    __tablename__ = "items"
    # access
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name: str = sqlalchemy.Column(sqlalchemy.String(100), nullable=True, unique=True)
    qty: int = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    price: float = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    active: bool = sqlalchemy.Column(sqlalchemy.Boolean, default=True, nullable=True)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )


engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
Base.metadata.create_all(bind=engine)
