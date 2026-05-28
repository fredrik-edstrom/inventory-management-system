import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Office


def create_office(offices: dict):
    office = Office(**offices)
    session.add(office)
    session.commit()


def remove_office(_id: int):
    office = session.query(Office).filter(Office.store_id == _id).first()
    session.delete(office)
    session.commit()


def update_office(_id: int, column: str, update: str):
    session.query(Office).filter(Office.store_id == _id).update({column: update})
    session.commit()


def get_office_by_id(_id: int) -> dict:
    offices = session.query(Office).filter(Office.store_id == _id).first()
    return {i.name: getattr(offices, i.name) for i in offices.table.columns}


def order_by_office(column: str) -> list:
    return [{
                'store_id': office.store_id,
                'name': office.name,
                'address': office.address,
                'zip_code': office.zip_code,
                'phone': office.phone
            } for office in session.query(Office).order_by(column)]


def search_for_office(column: str, search_for: str) -> list:
    offices = session.query(Office).all()
    return [{
                'store_id': office.store_id,
                'name': office.name,
                'address': office.address,
                'zip_code': office.zip_code,
                'phone': office.phone
            } for office in offices if re.search(search_for, getattr(office, column))]


def get_all_offices() -> list:
    offices = session.query(Office).all()
    return [{i.name: getattr(office, i.name) for i in office.__table__.columns} for office in offices]
