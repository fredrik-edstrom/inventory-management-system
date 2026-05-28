from application.dll.mysql_db.repository import customer_car_repository


def create_customer_car(customer_car: dict):
    customer_car_repository.create_customer_car(customer_car)


def remove_customer_car(vin_no: str):
    customer_car_repository.remove_customer_car(vin_no)


def update_customer_car(vin_no: str, column: str, update: str):
    customer_car_repository.update_customer_car(vin_no, column, update)


def get_customer_car_by_id(vin_no: str) -> dict:
    return customer_car_repository.get_customer_car_by_id(vin_no)


def order_by_customer_car(column: str) -> list:
    return customer_car_repository.order_by_customer_car(column)


def search_for_customer_car(column: str, search_for: str) -> list:
    return customer_car_repository.search_for_customer_car(column, search_for)


def get_all_customers_cars() -> list:
    return customer_car_repository.get_all_customer_cars()
