from application.dll.mongo.db import db
from application.dll.mongo.models import Document


class CarModel(Document):
    collection = db.cars


class Customer(Document):
    collection = db.customers


class Employee(Document):
    collection = db.employees


class Product(Document):
    collection = db.products


class Storage(Document):
    collection = db.storages
