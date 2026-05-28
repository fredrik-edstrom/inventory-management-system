from application.dll.mysql_db.repository import office_repository


def create_office(office: dict):
    office_repository.create_office(office)


def remove_office(_id: int):
    office_repository.remove_office(_id)


def update_office(_id: int, column: str, update: str):
    office_repository.update_office(_id, column, update)


def get_office_by_id(_id: int) -> dict:
    return office_repository.get_office_by_id(_id)


def order_by_office(column: str) -> list:
    return office_repository.order_by_office(column)


def search_for_office(column: str, search_for: str) -> list:
    return office_repository.search_for_office(column, search_for)


def get_all_offices() -> list:
    return office_repository.get_all_offices()
