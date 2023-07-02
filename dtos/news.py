from ctypes import Union
from typing import Optional
from pydantic import BaseModel
from dtos.shared import PagedParamsDto
from dtos.user import UserOutput

from datetime import datetime

class CreateNewsInput(BaseModel):
    title: str
    content: str
    image: str

class UpdateNewsInput(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None

class CreateNewsCommentInput(BaseModel):
    content: str
    news_id: int

class UpdateNewsCommentInput(BaseModel):
    content : Optional[str] = None

class GetNewsDto(PagedParamsDto):
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    user_id: Optional[int] = None

class NewsOutput(BaseModel):
    id: int
    title: str
    content: str
    image: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    user: UserOutput
    class Config:
        orm_mode = True
