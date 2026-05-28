import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Manufacturer


def create_manufacturer(manufacturer: dict):
    manufacturer = Manufacturer(**manufacturer)
    session.add(manufacturer)
    session.commit()


def remove_manufacturer(_id: int):
    manufacturer = session.query(Manufacturer).filter(Manufacturer.manufacturer_id == _id).first()
    session.delete(manufacturer)
    session.commit()


def update_manufacturer(_id: int, column: str, update: str):
    session.query(Manufacturer).filter(Manufacturer.manufacturer_id == _id).update({column: update})
    session.commit()


def get_manufacturer_by_id(_id: int):
    manufacturer = session.query(Manufacturer).filter(Manufacturer.manufacturer_id == _id).first()
    return {i.name: getattr(manufacturer, i.name) for i in manufacturer.table.columns}


def order_by_manufacturer(column: str):
    return [{
        'manufacturer_id': manufacturer.manufacurer_id,
        'company_name': manufacturer.company_name,
        'address': manufacturer.address,
        'city': manufacturer.city,
        'zip_code': manufacturer.zip_code,
        'phone': manufacturer.phone,
        'contact_id': manufacturer.contact_id
    } for manufacturer in session.query(Manufacturer).order_by(column)]


def search_for_manufacturer(column: str, search_for: str):
    manufacturers = session.query(Manufacturer).all()
    return [{
        'manufacturer_id': manufacturer.manufacurer_id,
        'company_name': manufacturer.company_name,
        'address': manufacturer.address,
        'city': manufacturer.city,
        'zip_code': manufacturer.zip_code,
        'phone': manufacturer.phone,
        'contact_id': manufacturer.contact_id
    } for manufacturer in manufacturers if re.search(search_for, getattr(manufacturer, column))]


def get_all_manufacturers():
    manufacturers = session.query(Manufacturer).all()
    return [{i.name: getattr(manufacturer, i.name) for i in manufacturer.__table__.columns} for manufacturer in manufacturers]
