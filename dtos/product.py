from typing import Optional
from pydantic import BaseModel

class CreateProductDTO(BaseModel):
    name: str
    description: str
    price: float
    image: str
    category_id: int

class UpdateProductDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    category_id: Optional[int] = None

class CreateProductDetailDTO(BaseModel):
    product_id: int
    name: str
    value: str
    quantity: int

class UpdateProductDetailDTO(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    quantity: Optional[int] = None
