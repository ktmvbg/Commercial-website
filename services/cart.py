from dtos import cart
from models import User, Product, CartProduct
from sqlalchemy.orm import Session, joinedload


def add_to_cart(session: Session, user_id: int, dto: cart.AddToCartDto):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')

    product = session.query(Product).filter_by(id=dto.product_id).first()
    if not product:
        return (False, 'Product does not exist')

    cart_product = session.query(CartProduct).filter(CartProduct.user_id == user_id, CartProduct.product_id == dto.product_id).first()
    
    if(cart_product):
        cart_product.quantity += dto.quantity
    else:
        cart_product = CartProduct(user_id=user_id, product_id=dto.product_id, quantity=dto.quantity)
        session.add(cart_product)

    session.commit()
    session.refresh(cart_product)
    return (True, cart_product)

def get_cart(session: Session, user_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')

    cart_products = session.query(CartProduct).filter(CartProduct.user_id==user_id).options(joinedload(CartProduct.product)).all()
    return (True, cart_products)

def remove_from_cart(session: Session, user_id: int, dto: cart.RemoveFromCartDto):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')

    cart_product = session.query(CartProduct).filter_by(user_id=user_id, product_id=dto.product_id).first()
    if not cart_product:
        return (False, 'Product does not exist in cart')

    session.delete(cart_product)
    session.commit()
    return (True, cart_product)

def update_cart(session: Session, user_id: int, dto: cart.UpdateCartDto):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')

    cart_product = session.query(CartProduct).filter_by(user_id=user_id, product_id=dto.product_id).first()
    if not cart_product:
        return (False, 'Product does not exist in cart')

    cart_product.quantity = dto.quantity
    session.commit()
    session.refresh(cart_product)
    return (True, cart_product)
    