from application.dll.mysql_db.repository import manufacturer_repository


def create_manufacturer(manufacturer: dict):
    manufacturer_repository.create_manufacturer(manufacturer)


def remove_manufacturer(_id: int):
    manufacturer_repository.remove_manufacturer(_id)


def update_manufacturer(_id: int, column: str, update: str):
    manufacturer_repository.update_manufacturer(_id, column, update)


def get_manufacturer_by_id(_id: int) -> dict:
    return manufacturer_repository.get_manufacturer_by_id(_id)


def order_by_manufacturer(column: str) -> list:
    return manufacturer_repository.order_by_manufacturer(column)


def search_for_manufacturer(column: str, search_for: str) -> list:
    return manufacturer_repository.search_for_manufacturer(column, search_for)
