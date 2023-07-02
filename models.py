from datetime import timedelta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    account_type = Column(Integer)  # 1 = user, 2 = admin
    username = Column(String(200), nullable=False)
    password = Column(String(1000), nullable=False)
    fullname = Column(String(200), nullable=False)
    
    status = Column(Integer, nullable=False) # 1 = active, 2 = inactive
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=False)
    
    # products = relationship('Product')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String(1000), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ProductDetail(Base):
    __tablename__ = 'product_details'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    name = Column(String(200), nullable=False)
    value = Column(String(1000), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    
    product = relationship('Product', backref='product_details')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    order_key = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    total = Column(Float, nullable=False)
    status = Column(Integer, nullable=False) # 1 = pending, 2 = completed, 3 = cancelled
    
    user = relationship('User', backref='orders')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class OrderProduct(Base):
    __tablename__ = 'order_products'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    price_per_unit = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    
    order = relationship('Order', backref='order_products')
    product = relationship('Product', backref='order_products')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class OrderProductDetail(Base):
    __tablename__ = 'order_product_details'
    
    id = Column(Integer, primary_key=True)
    order_product_id = Column(Integer, ForeignKey('order_products.id'))
    product_detail_id = Column(Integer, ForeignKey('product_details.id'))
    quantity = Column(Integer, nullable=False)
    
    order_product = relationship('OrderProduct', backref='order_product_details')
    product_detail = relationship('ProductDetail', backref='order_product_details')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class News(Base):
    __tablename__ = 'news'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000), nullable=False)
    image = Column(String(1000), nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class NewsComment(Base):
    __tablename__ = 'news_comments'
    
    id = Column(Integer, primary_key=True)
    content = Column(String(1000), nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    news_id = Column(Integer, ForeignKey('news.id'))
    
    user = relationship('User')
    news = relationship('News')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class CartProduct(Base):
    __tablename__ = 'cart_products'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    
    user = relationship('User')
    product = relationship('Product')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Coupon(Base):
    __tablename__ = 'coupons'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(1000), nullable=False)
    coupon_type = Column(Integer, nullable=False) # 1 = percentage, 2 = fixed
    discount = Column(Float, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    minimum_order = Column(Float, nullable=False)
    maximum_discount = Column(Float, nullable=False)
    number = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False) # 1 = active, 2 = inactive
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class CouponHistory(Base):
    __tablename__ = 'coupon_histories'
    
    id = Column(Integer, primary_key=True)
    coupon_id = Column(Integer, ForeignKey('coupons.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    
    coupon = relationship('Coupon', backref='coupon_histories')
    user = relationship('User', backref='coupon_histories')
    order = relationship('Order', backref='coupon_histories')
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())