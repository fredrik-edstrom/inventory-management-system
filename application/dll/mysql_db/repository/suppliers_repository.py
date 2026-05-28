import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Supplier


def create_suppliers(supplier: dict):
    supplier = Supplier(**supplier)
    session.add(supplier)
    session.commit()


def remove_supplier(_id: int):
    contact_person = session.query(Supplier).filter(Supplier.supplier_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_supplier(_id: int, column: str, update: str):
    session.query(Supplier).filter(Supplier.supplier_id == _id).update({column: update})
    session.commit()


def get_supplier_by_id(_id: int) -> dict:
    supplier = session.query(Supplier).filter(Supplier.supplier_id == _id).first()
    return {i.name: getattr(supplier, i.name) for i in supplier.table.columns}


def order_by_supplier(column: str) -> list:
    return [{
                'supplier_id': supplier.supplier_id,
                'company_name': supplier.company_name,
                'address': supplier.address,
                'city': supplier.city,
                'zip_code': supplier.zip_code,
                'contact_id': supplier.contact_id
            } for supplier in session.query(Supplier).order_by(column)]


def search_for_supplier(column: str, search_for: str) -> list:
    suppliers = session.query(Supplier).all()
    return [{
                'supplier_id': supplier.supplier_id,
                'company_name': supplier.company_name,
                'address': supplier.address,
                'city': supplier.city,
                'zip_code': supplier.zip_code,
                'contact_id': supplier.contact_id
            } for supplier in suppliers if re.search(search_for, getattr(supplier, column))]


def get_all_suppliers() -> list:
    suppliers = session.query(Supplier).all()
    return [{i.name: getattr(supplier, i.name) for i in supplier.__table__.columns} for supplier in suppliers]
