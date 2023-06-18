from models import Product, ProductDetail, Category
from dtos import product, shared
from sqlalchemy.orm import Session

def create_product(session: Session, product: product.CreateProductDto):
    is_category = session.query(Category).filter_by(id=product.category_id).first()
    if not is_category:
        return (False, 'Category does not exist')
    product = Product(name=product.name, description=product.description, price=product.price, image=product.image, category_id=product.category_id)
    session.add(product)
    session.commit()
    session.refresh(product)
    return (True, product)

def update_product(session: Session, product_id: int, product: product.UpdateProductDto):
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
    session.refresh(product_in_db)
    # return (True, "Updated {}".format(product.name))
    return (True, product_in_db)

def delete_product(session: Session, product_id: int):
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        return (False, 'Product does not exist')
    session.delete(product)
    session.commit()
    return (True, "Deleted {}".format(product.name))

def filter_products(session: Session, query: product.FilterProductsDto):
    products = session.query(Product)
    if query.search:
        products = products.filter(Product.name.contains(query.search))
    if query.category_id:
        products = products.filter(Product.category_id == query.category_id)
    if query.order_by:
        if query.order_by == 'name':
            if query.order == 'desc':
                products = products.order_by(Product.name.desc())
            else:
                products = products.order_by(Product.name.asc())
        elif query.order_by == 'price':
            if query.order == 'desc':
                products = products.order_by(Product.price.desc())
            else:
                products = products.order_by(Product.price.asc())
    products = products.offset((query.page-1)*query.page_size).limit(query.page_size).all()
    return products

def get_products(session: Session, page: int, limit: int):
    products = session.query(Product).offset((page-1)*limit).limit(limit).all()
    return products

def get_product(session: Session, product_id: int):
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        return (False, 'Product does not exist')
    return (True, product)

def create_product_detail(session: Session, product_detail: product.CreateProductDetailDto):
    product_detail = ProductDetail(product_id=product_detail.product_id, name = product_detail.name, value = product_detail.value, quantity = product_detail.quantity)
    session.add(product_detail)
    session.commit()
    return product_detail

def update_product_detail(session: Session, product_detail_id: int, product_detail: product.UpdateProductDetailDto):
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