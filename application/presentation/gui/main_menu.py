import PySimpleGUI as sg
import variables
from customer_windows import *


def main_menu():
    layout = [
        # Row 1
        [sg.Text('Rip and Ship', **h1)],

        # Row 2
        [sg.Text('Welcome to the employee portal, please select which table to view', **p)],

        # Row 3
        [sg.Button('Customers', **button1),
         sg.Button('Orders', **button1),
         sg.Button('Inventory', **button1)]
    ]

    return sg.Window('Rip & Ship', layout, **wdw)

