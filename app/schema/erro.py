from pydantic import BaseModel

class Error400(BaseModel):
    detail: str