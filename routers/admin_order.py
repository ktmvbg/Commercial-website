from fastapi import APIRouter, Depends, HTTPException, Request, status
from services import admin_order

from jose import JWTError
from dependencies import get_db, admin_middleware, admin_middleware
from sqlalchemy.orm import Session
from models import User
from dtos.order import  AdminGetOrdersDto


router = APIRouter(prefix="/api/admin/order", tags=["admin order"])


@router.get("/")
async def get_orders(request: Request, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    query = AdminGetOrdersDto(**request.query_params)
    success, result = admin_order.get_orders(db, query)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/{order_id}")
async def get_order_by_id(order_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = admin_order.get_order(db, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/{order_id}/cancel")
async def cancel_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = admin_order.reject_order(db, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/{order_id}/approve")
async def approve_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = admin_order.accept_order(db, order_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result
    