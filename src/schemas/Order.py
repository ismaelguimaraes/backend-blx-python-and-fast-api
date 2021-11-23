from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class OrderSchema(BaseModel):
    id: Optional[str] = str(uuid4())
    quantity: int
    is_delivery: Optional[bool] = True
    address: str
    observation: str

    class Config:
        orm_mode = True