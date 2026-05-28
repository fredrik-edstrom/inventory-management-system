import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Product, ProductFitsModel


def create_product(product: dict):
    products = Product(**product)
    session.add(products)
    session.commit()


def remove_product(_id: int):
    product = session.query(Product).filter(Product.product_id == _id).first()
    session.delete(product)
    session.commit()


def update_product(_id: int, column: str, update: str):
    session.query(Product).filter(Product.employee_id == _id).update({column: update})
    session.commit()


def get_product_by_id(_id: int) -> dict:
    product = session.query(Product).filter(Product.product_id == _id).first()
    return {i.name: getattr(product, i.name) for i in product.__table__.columns}


def order_by_product(column) -> list:
    return [{
                'product_id': product.product_id,
                'product_name': product.product_name,
                'description': product.description,
                'price_in': product.price_in
            } for product in session.query(Product).order_by(column)]


def search_for_product(column: str, search_for: str) -> list:
    products = session.query(Product).all()
    return [{
                'product_id': product.product_id,
                'product_name': product.product_name,
                'description': product.description,
                'price_in': product.price_in
            } for product in products if re.search(search_for, getattr(product, column))]


def get_all_products() -> list:
    products = session.query(Product).all()
    return [{i.name: getattr(product, i.name) for i in product.__table__.columns} for product in products]


def create_product_fit_models(product_fit_model: dict):
    product_fit_model = ProductFitsModel(**product_fit_model)
    session.add(product_fit_model)
    session.commit()
