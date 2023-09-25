from fastapi import APIRouter, Depends, HTTPException, Request, status
from services import news

from jose import JWTError
from dependencies import get_db, admin_middleware, admin_middleware
from sqlalchemy.orm import Session
from models import User
from dtos.news import  CreateNewsInput, UpdateNewsInput, GetNewsDto

router = APIRouter(prefix="/api/news", tags=["news"])

@router.post("/")
async def create_news(dto: CreateNewsInput, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = news.create_news(db, user.id, dto)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.patch("/{news_id}")
async def update_news(news_id: int, dto: UpdateNewsInput, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = news.update_news(db, news_id, user.id, dto)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result) 
    return result

@router.delete("/{news_id}")
async def delete_news(news_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = news.delete_news(db, news_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/")
async def get_news(request: Request, db: Session = Depends(get_db)):
    query = GetNewsDto(**request.query_params)
    success, result = news.get_news(db, query)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/{news_id}")
async def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    success, result = news.get_news_by_id(db, news_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result
    