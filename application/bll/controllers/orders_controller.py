from application.dll.mysql_db.repository import orders_repository


def create_orders(orders: dict):
    orders_repository.create_orders(orders)


def remove_order(_id: int):
    orders_repository.create_orders(_id)


def update_order(_id: int, column: str, update: str):
    orders_repository.update_order(_id, column, update)


def get_order_by_id(_id: int) -> dict:
    return orders_repository.get_order_by_id(_id)


def order_by_order(column: str) -> list:
    return orders_repository.order_by_order(column)


def search_for_order(column: str, search_for: str) -> list:
    return orders_repository.search_for_order(column, search_for)


def get_all_orders() -> list:
    return orders_repository.get_all_orders()


def create_order_details(order_details: dict):
    orders_repository.create_order_details(order_details)


def create_orders_from_manufacturers(order_from_manufacturer: dict):
    orders_repository.create_orders_from_manufacturers(order_from_manufacturer)


def create_orders_from_suppliers(order_from_supplier: dict):
    orders_repository.create_orders_from_suppliers(order_from_supplier)


def create_suppliers_orders_from(supplier_order_from: dict):
    orders_repository.create_suppliers_orders_from(supplier_order_from)

def get_all_temp_orders():
    return orders_repository.get_all_temp_orders()


def remove_temp_orders():
    orders_repository.clear_temps()