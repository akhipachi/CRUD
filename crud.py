from sqlalchemy.orm import Session
import models, schemas


def get_product_name(db: Session, name: str):
    return db.query(models.Products).filter(models.Products.name == name).all()



def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Products).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.Product):
    db_product = models.Products(name=product.name, brand_name=product.brand_name,
    regular_price_value=product.regular_price_value,offer_price_value=product.offer_price_value,
    currency=product.currency,classification_l1=product.classification_l1,
    classification_l2=product.classification_l2,classification_l3=product.classification_l3,
    classification_l4=product.classification_l4,image_url=product.image_url)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db:Session,name:str,product:schemas.ProductUpdate):
    db_update=db.query(models.Products).filter(models.Products.name==name).first()
    if db_update:
        for i in product.__dict__:
            if getattr(product,i):
                setattr(db_update,i,getattr(product,i))
            db.commit()
            db.refresh(db_update)
    return db_update

def delete_product(db:Session,name:str):
    db_delete=db.query(models.Products).filter(models.Products.name==name).all()
    if db_delete:
        for i in db_delete:
            db.delete(i)
        db.commit()
        return db_delete
    else:
        return