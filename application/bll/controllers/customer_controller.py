from application.dll.mongo.repository import customer_repository


def create_customer(customer: dict):
    customer_repository.create_customer(customer)


def remove_customer(_id: int):
    customer_repository.remove_customer(_id)


def update_customer(_id: int, column: str, update: str):
    customer_repository.update_customer(_id, column, update)


def get_customer_by_id(_id: int) -> dict:
    return customer_repository.get_customer_by_id(_id)


def order_by_customer(column: str) -> list:
    return customer_repository.order_by_customer(column)


def search_for_customer(column: str, search_for: str) -> list:
    return customer_repository.search_for_customer(column, search_for)


def get_all_customer() -> list:
    return customer_repository.get_all_customers()

