import PySimpleGUI as sg
from variables import *
from application.bll.controllers.orders_controller import *


def orders_window():
    data = [[value for value in d.values()] for d in get_all_orders()]
    header_list = [key for key in get_all_orders()[0]]
    layout = [

        # Row 1
        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Orders', **h1), sg.Text("", **h1), sg.Button('Search', font=('Sora SemiBold', 12))],

        # Row 2
        [sg.Table(values=data, headings=header_list, **table, key='-TABLE-', enable_events=True)],

        # Row 3
        [sg.Button('Place order', **button2),
         sg.Button('Cancel order', **button2),
         sg.Button('Edit order', **button2),
         ]
    ]

    return sg.Window('Table', layout, **wdw)


def place_order_window():
    layout = [

        [sg.Text('Order ID ', **h2), sg.In(key='order_id')],
        [sg.Text('Customer ID: ', **h2), sg.In(key='customer_id')],
        [sg.Text('Price: ', **h2), sg.In(key='price')],
        [sg.Text('Employee: ', **h2), sg.In(key='employee_id')],
        [sg.Text('Order date: ', **h2), sg.In(key='order_date')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Place order', **button2, key='-PLACE-', bind_return_key=True), sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Place order', layout, size=(500, 600), finalize=True, keep_on_top=True)


def edit_order_window(idx):

    layout = [
        [sg.Text('Order ID ', **h2), sg.In(default_text=idx[0], key='order_id')],
        [sg.Text('Customer ID: ', **h2), sg.In(default_text=idx[1], key='customer_id')],
        [sg.Text('Price: ', **h2), sg.In(default_text=idx[2], key='price')],
        [sg.Text('Employee: ', **h2), sg.In(default_text=idx[3], key='employee_id')],
        [sg.Text('Order date: ', **h2), sg.In(default_text=idx[4], key='order_date')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Submit', **button2, key='-EDIT-', bind_return_key=True),
         sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Edit order', layout, size=(500, 600), finalize=True, keep_on_top=True)

