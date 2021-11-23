from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class ProductSchema(BaseModel):
    id: Optional[str] = str(uuid4())
    name: str
    details: str
    price: float
    is_available: Optional[bool] = True

    class Config:
        orm_mode = True