from fastapi import APIRouter, Depends, HTTPException, status
from services import cart

from jose import JWTError
from dependencies import get_db, get_current_user
from sqlalchemy.orm import Session
from models import User
from dtos.cart import AddToCartDto, RemoveFromCartDto, UpdateCartDto


router = APIRouter(prefix="/api/cart", tags=["cart"])


@router.post("/")
async def add_to_cart(input: AddToCartDto, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = cart.add_to_cart(db, user.id, input)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/")
async def get_cart(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = cart.get_cart(db, user.id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.delete("/")
async def remove_from_cart(input: RemoveFromCartDto, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = cart.remove_from_cart(db, user.id, input)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.patch("/")
async def update_cart(input: UpdateCartDto, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = cart.update_cart(db, user.id, input)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.post("/clear")
async def clear(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success, result = cart.clear_cart(db, user.id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result