from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4

from schemas.Order import Order
from schemas.Product import Product

class User(BaseModel):
    id: Optional[str] = uuid4()
    name: str
    telephone: str
    email: str
    password: str
    is_provider: Optional[bool] = False
    is_admin: Optional[bool] = False

    class Config:
        orm_mode = True