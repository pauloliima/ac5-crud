from app.config.config import settings

from sqlalchemy import MetaData as MD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine(settings.database_uri)

Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

MetaData = MD()

Base = declarative_base(bind=Engine, metadata=MetaData)

# Dependency Injection or DI
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
