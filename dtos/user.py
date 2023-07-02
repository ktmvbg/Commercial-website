
from typing import List, Optional
from models import User
from pydantic import BaseModel

class UserOutput(BaseModel):
    id: int
    username: str
    fullname: str
    account_type: int

    class Config:
        orm_mode = True

class CreateUserInput(BaseModel):
    username: str
    fullname: str
    password: str
    account_type: int

class UpdateUserInput(BaseModel):
    username: Optional[str]
    fullname: Optional[str]
    password: Optional[str]
    account_type: Optional[int]

