from dtos import cart
from models import User, Product, CartProduct
from sqlalchemy.orm import Session


def add_to_cart(session: Session, user_id: int, dto: cart.AddToCartDto):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')

    product = session.query(Product).filter_by(id=dto.product_id).first()
    if not product:
        return (False, 'Product does not exist')
    