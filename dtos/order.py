from pydantic import BaseModel

class CreateOrder(BaseModel):
    product_id: int
    quantity: int
