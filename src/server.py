from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

## Importações referentes ao banco
from infra.sqlalchemy.config.database import get_db, create_connection

## Importações referentes a Produtos
from schemas.Product import Product as ProductSchema
from infra.sqlalchemy.repositories.ProductsRepositories import ProductsRepositories

app = FastAPI()

## Cria a conexão com o banco de dados
create_connection()

@app.get('/products')
def list_products(db: Session = Depends(get_db)):
    products = ProductsRepositories(db).listAll()
    return products

@app.post('/products')
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    created_product = ProductsRepositories(db).create(product)
    return created_product