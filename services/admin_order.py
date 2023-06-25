from dtos import order
from models import User, Product, Order, OrderProduct
from sqlalchemy.orm import Session, joinedload
import uuid


def get_orders(session: Session, dto: order.AdminGetOrdersDto):
    orders = session.query(Order).options(joinedload(Order.order_products), joinedload(Order.order_products, OrderProduct.product))
    if dto.from_date:
        orders = orders.filter(Order.created_at >= dto.from_date)
    
    if dto.to_date:
        orders = orders.filter(Order.created_at <= dto.to_date)
    
    if dto.status:
        orders = orders.filter(Order.status == dto.status)
    
    if dto.user_id:
        orders = orders.filter(Order.user_id == dto.user_id)
    
    orders = orders.order_by(Order.created_at.desc())
    orders = orders.offset((dto.page-1)*dto.page_size).limit(dto.page_size).all()
    return (True, orders)

def get_order(session: Session,  order_id: int):
    order = session.query(Order).filter(Order.id==order_id).options(joinedload(Order.order_products), joinedload(Order.order_products, OrderProduct.product)).first()
    if not order:
        return (False, 'Order does not exist')
    return (True, order)

def accept_order(session: Session, order_id: int):
    order = session.query(Order).filter(Order.id==order_id).first()
    if not order:
        return (False, 'Order does not exist')
    order.status = 2
    session.commit()
    session.refresh(order)
    return (True, order)

def reject_order(session: Session, order_id: int):
    order = session.query(Order).filter(Order.id==order_id).first()
    if not order:
        return (False, 'Order does not exist')
    order.status = 3
    session.commit()
    session.refresh(order)
    return (True, order)