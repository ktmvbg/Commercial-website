from models import Product, ProductDetail
from dtos import product
from sqlalchemy.orm import Session

def create_product(session: Session, product: product.CreateProductDTO):
    product = Product(name=product.name, description=product.description, price=product.price, image=product.image, category_id=product.category_id)
    session.add(product)
    session.commit()
    return product

def update_product(session: Session, product_id: int, product: product.UpdateProductDTO):
    product_in_db = session.query(Product).filter_by(id=product_id).first()
    if not product_in_db:
        return (False, 'Product does not exist')
    if (product.name):
        product_in_db.name = product.name
    if(product.description):
        product_in_db.description = product.description
    if(product.price):
        product_in_db.price = product.price
    if(product.image):
        product_in_db.image = product.image
    if(product.category_id):
        product_in_db.category_id = product.category_id
    
    session.commit()
    return (True, "Updated {}".format(product.name))

def delete_product(session: Session, product_id: int):
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        return (False, 'Product does not exist')
    session.delete(product)
    session.commit()
    return (True, "Deleted {}".format(product.name))

def get_products(session: Session, page: int, limit: int):
    products = session.query(Product).offset((page-1)*limit).limit(limit).all()
    return products

def get_product(session: Session, product_id: int):
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        return (False, 'Product does not exist')
    return product

def create_product_detail(session: Session, product_detail: product.CreateProductDetailDTO):
    product_detail = ProductDetail(product_id=product_detail.product_id, name = product_detail.name, value = product_detail.value, quantity = product_detail.quantity)
    session.add(product_detail)
    session.commit()
    return product_detail

def update_product_detail(session: Session, product_detail_id: int, product_detail: product.UpdateProductDetailDTO):
    product_detail_in_db = session.query(ProductDetail).filter_by(id=product_detail_id).first()
    if not product_detail_in_db:
        return (False, 'Product detail does not exist')
    if (product_detail.name):
        product_detail_in_db.name = product_detail.name
    if(product_detail.value):
        product_detail_in_db.value = product_detail.value
    if(product_detail.quantity):
        product_detail_in_db.quantity = product_detail.quantity
    
    session.commit()
    return (True, "Updated {}".format(product_detail.name))

def delete_product_detail(session: Session, product_detail_id: int):
    product_detail = session.query(ProductDetail).filter_by(id=product_detail_id).first()
    if not product_detail:
        return (False, 'Product detail does not exist')
    session.delete(product_detail)
    session.commit()
    return (True, "Deleted {}".format(product_detail.name))

def get_product_stock(session: Session, product_id: int):
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        return (False, 'Product does not exist')
    product_detail = session.query(ProductDetail).filter_by(product_id=product_id).all()
    quantity = 0
    for detail in product_detail:
        quantity += detail.quantity
    return quantity