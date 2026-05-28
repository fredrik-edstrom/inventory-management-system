import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import CarModel


def create_customer_car(customer_car: dict):
    customer_car = CarModel(**customer_car)
    session.add(customer_car)
    session.commit()


def remove_customer_car(vin_no: str):
    customer_car = session.query(CarModel).filter(CarModel.vin_no == vin_no).first()
    session.delete(customer_car)
    session.commit()


def update_customer_car(vin_no: str, column: str, update: str):
    session.query(CarModel).filter(CarModel.vin_no == vin_no).update({column: update})
    session.commit()


def get_customer_car_by_id(vin_no: str) -> dict:
    customer_car = session.query(CarModel).filter(CarModel.vin_no == vin_no).first()
    return {i.name: getattr(customer_car, i.name) for i in customer_car.table.columns}


def order_by_customer_car(column: str) -> list:
    return [{
                'vin_no': car.vin_no,
                'customer_id': car.customer_id,
                'color': car.color,
                'year': car.year,
                'model': car.model,
                'brand': car.brand
            } for car in session.query(CarModel).order_by(column)]


def search_for_customer_car(column: str, search_for: str) -> list:
    cars = session.query(CarModel).all()
    return [{
                'vin_no': car.vin_no,
                'customer_id': car.customer_id,
                'color': car.color,
                'year': car.year,
                'model': car.model,
                'brand': car.brand
            } for car in cars if re.search(search_for, getattr(car, column))]


def get_all_customer_cars() -> list:
    cars = session.query(CarModel).all()
    return [{i.name: getattr(car, i.name) for i in car.__table__.columns} for car in cars]
