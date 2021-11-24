from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from ..config.database import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    telephone = Column(String)
    email = Column(String)
    password = Column(String)
    is_provider = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    products = relationship('ProductModel', back_populates='user')