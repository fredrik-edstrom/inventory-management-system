import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Employee


def create_employee(employee: dict):
    employee = Employee(**employee)
    session.add(employee)
    session.commit()


def remove_employee(_id: int):
    employees = session.query(Employee).filter(Employee.employee_id == _id).first()
    session.delete(employees)
    session.commit()


def update_employee(_id: int, column: str, update: str):
    session.query(Employee).filter(Employee.employee_id == _id).update({column: update})
    session.commit()


def get_employee_by_id(_id: int) -> dict:
    employee = session.query(Employee).filter(Employee.employee_id == _id).first()
    return {i.name: getattr(employee, i.name) for i in employee.table.columns}


def order_by_employee(column: str) -> list:
    return [{
        'employee_id': employee.manufacurer_id,
        'company_name': employee.company_name,
        'address': employee.address,
        'city': employee.city,
        'zip_code': employee.zip_code,
        'phone': employee.phone,
        'contact_id': employee.contact_id
    } for employee in session.query(Employee).order_by(column)]


def search_for_employee(column: str, search_for: str) -> list:
    employees = session.query(Employee).all()
    return [{
        'employee_id': employee.manufacurer_id,
        'company_name': employee.company_name,
        'address': employee.address,
        'city': employee.city,
        'zip_code': employee.zip_code,
        'phone': employee.phone,
        'contact_id': employee.contact_id
    } for employee in employees if re.search(search_for, getattr(employee, column))]


def get_all_employees() -> list:
    employees = session.query(Employee).all()
    return [{i.name: getattr(employee, i.name) for i in employee.__table__.columns} for employee in employees]
