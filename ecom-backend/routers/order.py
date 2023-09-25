from fastapi import APIRouter, Depends, HTTPException, Request, status
from services import order

from jose import JWTError
from dependencies import get_db, get_current_user, admin_middleware
from sqlalchemy.orm import Session
from models import User
from dtos.order import CreateOrder, GetOrdersDto


router = APIRouter(prefix="/api/order", tags=["order"])


@router.get("/")
async def get_orders(request: Request, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    query = GetOrdersDto(**request.query_params)
    success, result = order.get_orders(db, user.id, query)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/")
async def create_order(input: CreateOrder, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = order.create_order(db, user.id, input)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/{order_id}")
async def get_order_by_id(order_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = order.get_order(db, user.id, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/{order_id}/cancel")
async def cancel_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = order.reject_order(db, user.id, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/{order_id}/approve")
async def approve_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = order.accept_order(db, user.id, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/{order_id}/confirm")
async def approve_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = order.accept_order(db, user.id, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result
    