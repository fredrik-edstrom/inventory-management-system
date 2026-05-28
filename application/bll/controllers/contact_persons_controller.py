from application.dll.mysql_db.repository import contact_persons_repository


def create_contact_person(contact_person: dict):
    contact_persons_repository.create_contact_person(contact_person)


def remove_contact_person(_id: int):
    contact_persons_repository.remove_contact_person(_id)


def update_contact_person(_id: int, column: str, update: str):
    contact_persons_repository.update_contact_person(_id, column, update)


def get_contact_person_by_id(_id: int) -> dict:
    return contact_persons_repository.get_contact_person_by_id(_id)


def order_by_contact_person(column: str) -> list:
    return contact_persons_repository.order_by_contact_person(column)


def search_for_contact_person(column: str, search_for: str) -> list:
    return contact_persons_repository.search_for_contact_person(column, search_for)


def get_all_contact_persons() -> list:
    return contact_persons_repository.get_all_contact_persons()
