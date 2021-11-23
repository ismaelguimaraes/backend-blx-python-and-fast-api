from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4

from models.Order import Order
from models.Product import Product

class User(BaseModel):
    id: Optional[str] = uuid4()
    name: str
    telephone: str
    email: str
    password: str
    products: List[Product]
    sales: List[Order]
    orders: List[Order]
    is_provider: Optional[bool] = False
    is_admin: Optional[bool] = False