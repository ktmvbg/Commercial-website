from fastapi import APIRouter, Depends, HTTPException, Request, status
from services import chat

from jose import JWTError
from dependencies import get_db, admin_middleware, get_current_user
from sqlalchemy.orm import Session
from models import User
from dtos.chat import CreateChatMessage, ResponseMessage

router = APIRouter(prefix="/api/chat", tags=["chat bot"])

@router.post("/")
async def create_chat_message(input: CreateChatMessage, db: Session = Depends(get_db)):
    msg = chat.create_chat_message(db, 2, input)
    resp = chat.response_message(db, msg.id)
    return resp
    # return ResponseMessage(id=resp.id, message=resp.response, created_at=resp.created_at.strftime("%Y-%m-%d %H:%M:%S"))

@router.post("/langchain")
async def create_chat_message(input: CreateChatMessage, db: Session = Depends(get_db)):
    msg = chat.create_chat_message(db, 2, input)
    resp = chat.langchain_response_message(db, msg.id)
    return resp
    # return ResponseMessage(id=resp.id, message=resp.response, created_at=resp.created_at.strftime("%Y-%m-%d %H:%M:%S"))