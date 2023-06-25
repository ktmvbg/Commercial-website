from datetime import datetime
from pydantic import BaseModel
from dtos.shared import PagedParamsDto

class AdminGetOrdersDto(PagedParamsDto):
    from_date: datetime = None
    to_date: datetime = None
    user_id: int = None
    status: int = None

class GetOrdersDto(PagedParamsDto):
    from_date: datetime = None
    to_date: datetime = None
    status: int = None

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class CreateOrder(BaseModel):
    products: list[OrderItem]

class OrderItemOutput(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price_per_unit: float
    total: float

class OrderOutput(BaseModel):
    id: int
    order_key: str
    total: float
    products: list[OrderItemOutput]