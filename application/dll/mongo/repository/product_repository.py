import re

from application.dll.mongo.models.sub_models import Product


def create_product(product, manufacturer=None, supplier=None):
    if manufacturer:
        product['manufacturer'] = [i for i in manufacturer]
    if supplier:
        product['supplier'] = [i for i in supplier]
    product = Product(product)
    product.save()


def remove_product(**kwargs):
    product = Product.find(**kwargs).first()
    product.delete()


def update_product(column: str, update, **kwargs):
    product = Product.find(**kwargs).first()
    product = Product(**product.__dict__)
    product.__setattr__(column, update)
    product.save()


def order_by_product(column: str) -> list:
    return [product for product in Product.order_by(column)]


def search_for_product(column: str, search_for) -> list:
    return [product.__dict__ for product in Product.get_all() if re.search(search_for, getattr(Product, column))]


def get_all_products() -> list:
    return [product.__dict__ for product in Product.get_all()]


def get_product_id(**kwargs) -> list:
    return Product.get_object_id(**kwargs)


print(get_product_id(price_in=423))

