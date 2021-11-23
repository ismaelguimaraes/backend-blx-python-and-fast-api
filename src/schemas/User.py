from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4

class UserSchema(BaseModel):
    id: Optional[str] = str(uuid4())
    name: str
    telephone: str
    email: str
    password: str
    is_provider: Optional[bool] = False
    is_admin: Optional[bool] = False

    class Config:
        orm_mode = True