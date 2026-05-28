from variables import *
from application.bll.controllers.storages_controller import *


def inventory_window():

    data = [[value for value in d.values()] for d in get_all_storages()]
    orderdata = [[value for value in d.values()] for d in get_all_temp_orders()]
    header_list = [key for key in get_all_storages()[0]]
    ord_header_list = ['Shelf_id', 'Quantity ordered', 'Total price', 'product_id']
    if len(orderdata) == 0:
        orderdata = ['No Orders Placed Yet']
    layout = [

        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Inventory', **h1), sg.Text("", **h1),
         sg.Button('Search', font=('Sora SemiBold', 12))],

        # Inventory Table
        [sg.Table(values=data, headings=header_list, **table, key='-TABLE-', enable_events=True)],
        [sg.Button('Add item', **button2),
         sg.Button('Delete item', **button2),
         sg.Button('Update item', **button2)
         ],

        [sg.Text('Pending orders', **h1)],
        [sg.Table(values=orderdata, headings=ord_header_list, **table, key='-TABLE-', enable_events=True)],

        [sg.Button('Approve orders', **button2),
         sg.Button('Delete order', **button2),
         sg.Button('Edit order', **button2)
         ]
    ]

    return sg.Window('Table', layout, **wdw)


def edit_item_window():
    layout = [
        [sg.DropDown(['units_in_stock', 'capacity', 'product_id'],
                     default_value='units_in_stock', readonly=True, k='col'),
         sg.In(default_text='Please enter a new value', key='value'),
         sg.Button('Submit'), sg.Button('Cancel')]]

    return sg.Window(f"Edit item ... ", layout, size=(600, 100), finalize=True, keep_on_top=True)


def add_item_window():
    layout = [

        [sg.Text('Units_in_stock: ', **h2), sg.In(key='units_in_stock')],
        [sg.Text('capacity: ', **h2), sg.In(key='capacity')],
        [sg.Text('product_id: ', **h2), sg.In(key='product_id')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Add to inventory', **button2, key='-ADD-', bind_return_key=True), sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Add Customer', layout, size=(500, 600), finalize=True, keep_on_top=True)

def search_item_window(results):
    layout = [
        [sg.DropDown(['shelf_id', 'units_in_stock', 'capacity', 'product_id'],
                     default_value='units_in_stock', readonly=True, k='col'),
         sg.In(default_text='Please enter a new value', key='value'),
         sg.Button('Submit'), sg.Button('Cancel')],
        [sg.Table(values=results, headings=[key for key in get_all_storages()[0]], **table)]]


    return sg.Window(f"search item ... ", layout, size=(600, 100), finalize=True, keep_on_top=True)
