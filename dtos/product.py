from typing import Optional
from pydantic import BaseModel, validator
from dtos.shared import PagedParamsDto

class CreateProductDto(BaseModel):
    name: str
    description: str
    price: float
    image: str
    category_id: int
    
    @validator('price')
    def price_must_be_positive(cls, value):
        assert value > 0, 'price must be positive'
        return value
    

class UpdateProductDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    category_id: Optional[int] = None
    @validator('price')
    def price_must_be_positive(cls, value):
        assert value > 0, 'price must be positive'
        return value

class CreateProductDetailDto(BaseModel):
    product_id: int
    name: str
    value: str
    quantity: int

class UpdateProductDetailDto(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    quantity: Optional[int] = None

class FilterProductsDto(PagedParamsDto):
    category_id: Optional[int] = None