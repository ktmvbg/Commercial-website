from pydantic import BaseModel


class CreateChatMessage(BaseModel):
    message: str

class ResponseMessage(BaseModel):
    id: int
    message: str
    created_at: str