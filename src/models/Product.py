from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

from models.User import User

class Product(BaseModel):
    id: Optional[str] = uuid4()
    name: str
    owner: User
    details: str
    price: str
    is_available: bool