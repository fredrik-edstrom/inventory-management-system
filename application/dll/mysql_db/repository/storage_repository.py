import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Storage


def create_storages(storage: dict):
    storage = Storage(**storage)
    session.add(storage)
    session.commit()


def remove_storage(_id: int):
    contact_person = session.query(Storage).filter(Storage.shelf_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_storage(_id: int, column: str, update: str):
    session.query(Storage).filter(Storage.shelf_id == _id).update({column: update})
    session.commit()


def get_storage_by_id(_id: int) -> dict:
    storage = session.query(Storage).filter(Storage.storage_id == _id).first()
    return {i.name: getattr(storage, i.name) for i in storage.table.columns}


def order_by_storage(column: str) -> list:
    return [{
                'shelf_id': storage.shelf_id,
                'units_in_stock': storage.units_in_stock,
                'capacity': storage.capacity,
                'product_id': storage.product_id
            } for storage in session.query(Storage).order_by(column)]


def search_for_storage(column: str, search_for: str) -> list:
    storages = session.query(Storage).all()
    return [{
                'shelf_id': storage.shelf_id,
                'units_in_stock': storage.units_in_stock,
                'capacity': storage.capacity,
                'product_id': storage.product_id
            } for storage in storages if re.search(search_for, getattr(storage, column))]


def get_all_storages() -> list:
    storages = session.query(Storage).all()
    return [{i.name: getattr(storage, i.name) for i in storage.__table__.columns} for storage in storages]


