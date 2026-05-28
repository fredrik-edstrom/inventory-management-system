from variables import *
from application.bll.controllers.customer_controller import get_all_customer



def edit_customer(row, output):
    data[row] = output


def place_order(output):
    order_data.append(output)


def edit_item(row, output):
    inventory_data[row] = output


def edit_order(row, output):
    order_data[row] = output


def add_item(output):
    inventory_data.append(output)


