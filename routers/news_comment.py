from fastapi import APIRouter, Depends, HTTPException, Request, status
from services import news_comment

from jose import JWTError
from dependencies import get_db, admin_middleware, get_current_user
from sqlalchemy.orm import Session
from models import User
from dtos.news import CreateNewsCommentInput, UpdateNewsCommentInput, GetNewsCommentDto

router = APIRouter(prefix="/api/news-comment", tags=["news comment"])

@router.post("/")
async def create_comment(dto: CreateNewsCommentInput, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = news_comment.create_comment(db, user.id, dto)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result    

@router.patch("/{comment_id}")
async def update_comment(comment_id: int, dto: UpdateNewsCommentInput, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = news_comment.update_comment(db, comment_id, user.id, dto)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.delete("/{comment_id}")
async def delete_comment(comment_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = news_comment.delete_comment(db, comment_id, user.id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/{news_id}")
async def get_comments(news_id: int, request: Request, db: Session = Depends(get_db)):
    query = GetNewsCommentDto(**request.query_params)
    success, result = news_comment.get_comments(db, news_id, query)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result
    