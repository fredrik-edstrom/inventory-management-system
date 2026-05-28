import re
from application.dll.mongo.models.sub_models import Employee


def create_employee(employee: dict, office=None):
    if office:
        employee['office'] = office
    employee = Employee(employee)
    employee.save()


def remove_employee(**kwargs):
    employee = Employee.find(**kwargs).first()
    employee.delete()


def update_employee(column: str, update, **kwargs):
    employee = Employee.find(**kwargs).first()
    employee = Employee(**employee.__dict__)
    employee.__setattr__(column, update)
    employee.save()


def order_by_employee(column: str) -> list:
    return [employee for employee in Employee.order_by(column)]


def search_for_employee(column: str, search_for) -> list:
    return [employee.__dict__ for employee in Employee.get_all() if re.search(search_for, getattr(employee, column))]


def get_all_employees() -> list:
    return [employee.__dict__ for employee in Employee.get_all()]


def get_employee_id(**kwargs) -> list:
    return Employee.get_object_id(**kwargs)
