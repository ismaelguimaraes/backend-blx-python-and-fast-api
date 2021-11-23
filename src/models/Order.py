from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

from models.User import User
from models.Product import Product

class Order(BaseModel):
    id: Optional[str] = uuid4()
    user: User
    product: Product
    quantity: int
    is_delivery: Optional[bool] = True
    address: str
    observation: str