from application.dll.mysql_db.repository import product_repository


def create_product(product: dict):
    product_repository.create_product(product)


def remove_product(_id: int):
    product_repository.remove_product(_id)


def update_product(_id: int, column: str, update: str):
    product_repository.update_product(_id, column, update)


def get_product_by_id(_id: int) -> dict:
    return product_repository.get_product_by_id(_id)


def order_by_product(column: str) -> list:
    return product_repository.order_by_product(column)


def search_for_product(column: str, search_for: str) -> list:
    return product_repository.search_for_product(column, search_for)


def get_all_product() -> list:
    return product_repository.get_all_products()


def create_product_fit_models(product_fit_model: dict):
    product_repository.create_product_fit_models(product_fit_model)


