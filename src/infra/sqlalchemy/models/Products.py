from sqlalchemy import Column, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..config.database import Base

class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    is_available = Column(Boolean, default=True)

    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('UserModel', back_populates='products')