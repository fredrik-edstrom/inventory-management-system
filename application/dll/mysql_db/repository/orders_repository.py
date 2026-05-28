import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Order,OrderDetail, OrderFromSupplier,\
    OrderFromManufacturer, SupplierOrdersFrom, TempOrders



def create_orders(orders: dict):
    orders = Order(**orders)
    session.add(orders)
    session.commit()


def remove_order(_id: int):
    contact_person = session.query(Order).filter(Order.order_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_order(_id: int, column: str, update: str):
    session.query(Order).filter(Order.order_id == _id).update({column: update})
    session.commit()


def get_order_by_id(_id: int):
    order = session.query(Order).filter(Order.order_id == _id).first()
    return {i.name: getattr(order, i.name) for i in order.table.columns}


def order_by_order(column: str) -> list:
    return [{
                'order_id': order.order_id,
                'order_date': order.order_date,
                'delivery_date': order.delivery_date,
                'customer_id': order.customer_id,
                'employee_id': order.employee_id
            } for order in session.query(Order).order_by(column)]


def search_for_order(column: str, search_for: str) -> list:
    orders = session.query(Order).all()
    return [{
                'order_id': order.order_id,
                'order_date': order.order_date,
                'delivery_date': order.delivery_date,
                'customer_id': order.customer_id,
                'employee_id': order.employee_id
            } for order in orders if re.search(search_for, getattr(order, column))]


def get_all_orders() -> list:
    orders = session.query(Order).all()
    return [{i.name: getattr(order, i.name) for i in order.__table__.columns} for order in orders]


def create_order_details(order_details: dict):
    order_details = OrderDetail(**order_details)
    session.add(order_details)
    session.commit()


def get_all_order_details() -> list:
    order_details = session.query(OrderDetail).all()
    return [{i.name: getattr(order_detail, i.name) for i in order_detail.__table__.columns} for order_detail in order_details]


def create_orders_from_manufacturers(order_from_manufacturer: dict):
    order_from_manufacturer = OrderFromManufacturer(**order_from_manufacturer)
    session.add(order_from_manufacturer)
    session.commit()


def create_orders_from_suppliers(order_from_supplier: dict):
    order_from_supplier = OrderFromSupplier(**order_from_supplier)
    session.add(order_from_supplier)
    session.commit()


def create_suppliers_orders_from(supplier_order_from: dict):
    supplier_order_from = SupplierOrdersFrom(**supplier_order_from)
    session.add(supplier_order_from)
    session.commit()


def get_all_temp_orders() -> list:
    temp_orders = session.query(TempOrders).all()
    return [{i.name: getattr(temporder, i.name) for i in temporder.__table__.columns} for temporder in temp_orders]

def clear_temps():
    temps = session.query(TempOrders).all()
    [session.delete(temp) for temp in temps]
    session.commit()