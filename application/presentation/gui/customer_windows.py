import PySimpleGUI as sg
from variables import *
from application.bll.controllers import customer_controller
from application.bll.controllers.customer_controller import search_for_customer


def customer_window():
    data = [[value for value in d.values()] for d in get_all_customer()]
    header_list = [key for key in get_all_customer()[0]]

    layout = [
        # Row 1
        [sg.Button('Back', **button2), sg.Text("", **h1), sg.Text('Customers', **h1), sg.Text("", **h1),
         sg.Button('Search', font=('Sora SemiBold', 12))],
        # Row 2
        [sg.Table(values=data, headings=header_list, **table, key='-TABLE-', enable_events=True)],
        # Row 3
        [sg.Button('Add Customer', **button2),
         sg.Button('Remove Customer', **button2),
         sg.Button('Edit Customer', **button2), sg.Text("", **filler)
         ]
    ]

    return sg.Window('Customer Table', layout, **wdw)


def add_customer_window():
    layout = [

        [sg.Text('Company Name: ', **h2), sg.In(key='company_name')],
        [sg.Text('First Name: ', **h2), sg.In(key='first_name')],
        [sg.Text('Last Name: ', **h2), sg.In(key='last_name')],
        [sg.Text('Address: ', **h2), sg.In(key='address')],
        [sg.Text('City: ', **h2), sg.In(key='city')],
        [sg.Text('Zip-code: ', **h2), sg.In(key='zip_code')],
        [sg.Text('Phone No: ', **h2), sg.In(key='phone')],
        [sg.Text('E-mail: ', **h2), sg.In(key='email')],

        # Bottom row
        [sg.Text("", **h2), sg.Button('Add Customer', **button2, key='-ADD-', bind_return_key=True),
         sg.Button('Cancel', **button2)]
    ]
    return sg.Window('Add Customer', layout, size=(500, 600), finalize=True, keep_on_top=True)


def edit_customer_window():
    layout = [
        [sg.DropDown(['company_name', 'first_name', 'last_name', 'address', 'city', 'zip_code', 'phone', 'email'],
                     default_value='company_name', readonly=True, k='col'),
         sg.In(default_text='Please enter a new value', key='value'),
         sg.Button('Submit'), sg.Button('Cancel')]]

    return sg.Window(f"Edit Customer ... ", layout, size=(600, 100), finalize=True, keep_on_top=True)


def search_cust_window(results):
    layout = [
        [sg.DropDown(['first_name', 'last_name', 'address', 'city', 'zip_code', 'phone', 'email'],
                     default_value='first_name', readonly=True, k='col'),
         sg.In(default_text='Please enter a new value', key='value'),

         sg.Button('Search'), sg.Button('Cancel')],
        [sg.Table(values=results, headings=[key for key in get_all_customer()[0]], **table)]]

    return sg.Window("search Customer ... ", layout, size=(1800, 775), finalize=True, keep_on_top=True)
