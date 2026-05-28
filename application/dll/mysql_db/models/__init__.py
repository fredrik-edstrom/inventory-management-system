from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from application.dll.mysql_db.db import Base


class CarModel(Base):
    __tablename__ = 'customer_cars_models'

    vin_no = Column(Integer, primary_key=True, unique=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    color = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)
    model = Column(String(45), nullable=False)
    brand = Column(String(45), nullable=False)
    customer = relationship = relationship('Customer', back_populates='cars')


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(45), nullable=False)
    description = Column(String(45))
    price_in = Column(Integer, nullable=False)
    order_details = relationship('OrderDetail', back_populates='products')


class ProductFitsModel(Base):
    __tablename__ = 'products_fits_models'

    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    vin_no = Column(Integer, ForeignKey('customer_cars_models.vin_no'), primary_key=True)
    products = relationship('Product')
    cars = relationship('CarModel')


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact_persons.contact_id'))
    contact_persons = relationship('ContactPerson', back_populates='manufacturer')


class Office(Base):
    __tablename__ = 'offices'

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    employee = relationship('Employee', back_populates='offices')


class Storage(Base):
    __tablename__ = 'storages'

    shelf_id = Column(Integer, primary_key=True, autoincrement=True)
    units_in_stock = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    products = relationship('Product')


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact_persons.contact_id'))
    contact_persons = relationship('ContactPerson', back_populates='supplier')


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    customer = relationship('Customer', back_populates='orders')
    employee = relationship('Employee', back_populates='orders')
    order_details = relationship('OrderDetail')


class OrderDetail(Base):
    __tablename__ = 'orderdetails'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_each = Column(Integer, nullable=False)
    orders = relationship('Order', back_populates='order_details')
    products = relationship('Product', back_populates='order_details')


class OrderFromManufacturer(Base):
    __tablename__ = 'orders_from_manufacturers'

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('Product')
    manufacturers = relationship('Manufacturer')


class OrderFromSupplier(Base):
    __tablename__ = 'orders_from_suppliers'

    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('Product')
    suppliers = relationship('Supplier')


class SupplierOrdersFrom(Base):
    __tablename__ = 'suppliers_orders_from'

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'), primary_key=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
    manufacturer = relationship('Manufacturer')
    suppliers = relationship('Supplier')


class ContactPerson(Base):
    __tablename__ = 'contact_persons'

    contact_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    manufacturer = relationship('Manufacturer', back_populates='contact_persons')
    supplier = relationship('Supplier', back_populates='contact_persons')


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    cars = relationship('CarModel', back_populates='customer')
    orders = relationship('Order', back_populates='customer')


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    store_id = Column(Integer, ForeignKey('offices.store_id'))
    offices = relationship('Office', back_populates='employee')
    orders = relationship('Order', back_populates='employee')


class TempOrders(Base):
    __tablename__ = 'temp_order'
    shelf_id = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)
    total = Column(Integer, nullable=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('Product')

