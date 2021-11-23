from sqlalchemy.orm import Session

from schemas.Product import Product as ProductSchema
from infra.sqlalchemy.models.Products import Product as ProductModel

class ProductsRepositories():
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductSchema):
        db_product = ProductModel(
            id=product.id,
            name=product.name,
            details=product.details,
            price=product.price,
            is_available=product.is_available
        )

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def listAll(self):
        products = self.db.query(ProductModel).all()
        return products
    
    def listById(self):
        pass

    def delete(self):
        pass