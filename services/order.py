from dtos import order
from models import User, Product, Order, OrderProduct
from sqlalchemy.orm import Session, joinedload
import uuid

def create_order(session: Session, user_id: int, dto: order.CreateOrder):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')

    order = Order(user_id=user_id, status = 1, order_key = uuid.uuid4().hex)
    session.add(order)
    order.total = 0
    session.commit()
    session.refresh(order)
    total = 0
    for product in dto.products:
        p = session.query(Product).filter_by(id=product.product_id).first()
        if not p:
            return (False, 'Product does not exist')

        order_product = OrderProduct(order_id=order.id, product_id=p.id, quantity=product.quantity, price_per_unit = p.price, total = p.price * product.quantity)
        session.add(order_product)
        total += order_product.total
    order.total = total
    session.commit()
    
    session.refresh(order)
    return (True, order)

def get_orders(session: Session, user_id: int, dto: order.GetOrdersDto):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        return (False, 'User does not exist')
    orders = session.query(Order).filter(Order.user_id==user_id).options(joinedload(Order.order_products), joinedload(Order.order_products, OrderProduct.product))
    if dto.from_date:
        orders = orders.filter(Order.created_at >= dto.from_date)
    
    if dto.to_date:
        orders = orders.filter(Order.created_at <= dto.to_date)
        
    if dto.status:
        orders = orders.filter(Order.status == dto.status)   
         
    orders = orders.order_by(Order.created_at.desc())
    orders = orders.offset((dto.page-1)*dto.page_size).limit(dto.page_size).all()
    return (True, orders)

def get_order(session: Session, user_id: int, order_id: int):
    order = session.query(Order).filter(Order.user_id==user_id, Order.id==order_id).options(joinedload(Order.order_products), joinedload(Order.order_products, OrderProduct.product)).first()
    if not order:
        return (False, 'Order does not exist')
    return (True, order)
