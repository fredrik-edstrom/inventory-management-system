from application.dll.mysql_db.repository import employee_repository


def create_employee(employee: dict):
    employee_repository.create_employee(employee)


def remove_employee(_id: int):
    employee_repository.remove_employee(_id)


def update_employee(_id: int, column: str, update: str):
    employee_repository.update_employee(_id, column, update)


def get_employee_by_id(_id: int) -> dict:
    return employee_repository.get_employee_by_id(_id)


def order_by_employee(column: str) -> list:
    return employee_repository.order_by_employee(column)


def search_for_employee(column: str, search_for: str) -> list:
    return employee_repository.search_for_employee(column, search_for)


def get_all_employees() -> list:
    return employee_repository.get_all_employees()
