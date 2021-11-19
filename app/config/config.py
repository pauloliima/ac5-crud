from os import getenv as _ge
from pydantic import BaseSettings as _BS


class _Settings(_BS):
    database_uri: str = _ge("DATABASE_URI")
    api_v1: str = "/v1"
    
settings = _Settings()
