from pydantic import BaseModel


class AddToCartDto(BaseModel):
    product_id: int
    quantity: int

class UpdateCartDto(BaseModel):
    product_id: int
    quantity: int

class RemoveFromCartDto(BaseModel):
    product_id: int