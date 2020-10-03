from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Products(Base):
    __tablename__ = "Products"

    id = Column(Integer,index=True,primary_key=True)
    name = Column(String, index=True)
    brand_name = Column(String, index=True)
    regular_price_value = Column(Integer, index=True)
    offer_price_value = Column(Integer, index=True)
    currency = Column(String, index=True)
    classification_l1 = Column(String, index=True)
    classification_l2 = Column(String, index=True)
    classification_l3 = Column(String, index=True)
    classification_l4 = Column(String, index=True)
    image_url = Column(String, index=True)

