import re
from application.dll.mongo.models.sub_models import CarModel, Product


def create_customer_car(customer_car: dict, products=None):
    if products:
        customer_car['compatible_products'] = [product for product in products]
    customer_car = CarModel(customer_car)
    customer_car.save()


def remove_customer_car(vin_no: str):
    car = CarModel.find(vin_no=vin_no).first()
    car.delete()


def update_customer_car(column: str, update, **kwargs):
    car = CarModel.find(**kwargs).first()
    car = CarModel(**car.__dict__)
    car.__setattr__(column, update)
    car.save()


def order_by_customer_car(column: str) -> list:
    return [car for car in CarModel.order_by(column)]


def search_for_customer_cars(column: str, search_for) -> list:
    return [car.__dict__ for car in CarModel.get_all() if re.search(search_for, getattr(car, column))]


def get_all_customer_cars() -> list:
    return [car.__dict__ for car in CarModel.get_all()]


def get_customer_car_id(**kwargs) -> list:
    return CarModel.get_object_id(**kwargs)

