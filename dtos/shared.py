from typing import Optional
from pydantic import BaseModel

class PagedParamsDto(BaseModel):
    page: int = 1
    page_size: int = 10
    order_by: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None