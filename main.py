from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/products/{name}", response_model=List[schemas.Product])
def read_product(name: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_name(db, name=name)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{name}", response_model=schemas.ProductUpdate)
def update_product(name:str,product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_update=crud.update_product(db,name,product)
    if db_update:
        return db_update
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{name}")
def delete_product(name:str,db: Session = Depends(get_db)):
    delete_product=crud.delete_product(db,name=name)
    if delete_product:
        return {'No of records deleted':len(delete_product)}
    else:
        raise HTTPException(status_code=404, detail="Product not found")