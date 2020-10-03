from typing import List, Optional,Any

from pydantic import BaseModel


class Product(BaseModel):
    id:Optional[int]
    name : str
    brand_name : Optional[str]
    regular_price_value : int
    offer_price_value : int
    currency : str
    classification_l1 : Optional[str]
    classification_l2 : Optional[str]
    classification_l3 : Optional[str]
    classification_l4 : Optional[str]
    image_url : str

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name : Optional[str]
    brand_name : Optional[str]
    regular_price_value : Optional[int]
    offer_price_value : Optional[int]
    currency : Optional[str]
    classification_l1 : Optional[str]
    classification_l2 : Optional[str]
    classification_l3 : Optional[str]
    classification_l4 : Optional[str]
    image_url : Optional[str]

    class Config:
        orm_mode = True
'''

class UserBase(BaseModel):
    email: str



class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True'''