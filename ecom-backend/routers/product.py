from fastapi import APIRouter, Depends, HTTPException, status, Request
from services import product

from jose import JWTError
from dependencies import get_db, get_current_user, admin_middleware
from sqlalchemy.orm import Session
from models import User
from dtos.product import CreateProductDto, UpdateProductDto, FilterProductsDto

router = APIRouter(prefix="/api/products", tags=["product"])

@router.post("/")
async def create_product(input: CreateProductDto, db: Session = Depends(get_db), user: User = Depends(admin_middleware), ):
    success, result = product.create_product(db, input)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.get("/")
async def get_products(request: Request, db: Session = Depends(get_db)):
    query = FilterProductsDto(**request.query_params)
    result = product.filter_products(db, query)
    return result

@router.get("/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    success, result = product.get_product(db, product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.patch("/{product_id}")
async def update_product(product_id: int, input: UpdateProductDto, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = product.update_product(db, product_id, input)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db), user: User = Depends(admin_middleware)):
    success, result = product.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result
