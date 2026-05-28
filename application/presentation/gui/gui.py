import PySimpleGUI as sg

sg.theme("Dark Green 4")


button = {'size': (10, 2), 'font': ('Helvetica', 15, 'bold')}
button2 = {'font': ('Helvetica', 12, 'bold')}
tf = {'size': (10, 1), 'font': ("Helvetica", 12, 'bold')}
h1 = {'size': (30, 1),'justification': 'c','font':('Helvetica', 28, 'bold')}


def frontpage_window():
    layout = [
        [sg.Text('Rip and Ship', **h1)] ,
        [sg.Text('Welcome to the employee portal, please select which table to view',
                 size=(30, 2),
                 justification='c',
                 font=('Helvetica', 12))],
        [sg.Text('        ',
                 size=(30, 1),
                 justification='c',
                 font=('Helvetica', 15, 'bold'))],

        [sg.Button('Customers', **button),
         sg.Button('Orders', **button),
         sg.Button('Inventory', **button)]
    ]

    return sg.Window('Rip and Ship', layout,
                     finalize=True,
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def customer_window():
    header_list = ["First Name", "Last Name", "Address", "Phone", "e-mail"]
    layout = [
        [sg.Button('Back', **button2),

         sg.Text('Customers',**h1),
         sg.Text("", **tf)
         ],
        [sg.Table(values=data,
                  headings=header_list,
                  auto_size_columns=False,
                  def_col_width=12,
                  num_rows=min(25, len(data)),
                  font="Helvetica",
                  justification='c')
         ],
        [
            sg.Button('Add Customer', **button2),
            sg.Button('Remove Customer', **button2),
            sg.Button('Update Customer', **button2)
        ]
    ]

    return sg.Window('Customers', layout,
                     finalize=True,
                     size=(900, 600),
                     resizable=True,
                     element_justification='center')


def order_window():
    data = []
    header_list = []
    layout = [
        [
            sg.Text('Orders', **h1)
        ],

        [sg.Button('Back', **button2)],

        [sg.Table(values=data,
                  headings=header_list,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]
    return sg.Window('Orders', layout,
                     finalize=True,
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def inventory_window():
    layout = [
        [sg.Text('Inventory', **h1)],

        [sg.Button('Back', **button2)]
    ]
    return sg.Window('Inventory', layout,
                     finalize=True,
                     size=(500, 400),
                     resizable=True,
                     element_justification='center')


def add_customer_window():


    layout = [
        [sg.Text('First Name', **tf), sg.In(key="first_name")],
        [sg.Text('Last Name:', **tf), sg.In(key="last_name")],
        [sg.Text('Address: ', **tf), sg.In(key="address")],
        [sg.Text('City: ', **tf), sg.In(key="city")],
        [sg.Text('Zip-code: ', **tf), sg.In(key="zip_code")],
        [sg.Text('Phone No: ', **tf), sg.In(key="phone")],
        [sg.Text('E-mail: ', **tf), sg.In(key="email")],

        [sg.Button('Add Customer', **button2), sg.Button('Cancel', **button2)]
    ]

    return sg.Window('Add Customer', layout,
                     finalize=True,
                     size=(500, 400),
                     resizable=True,
                     element_justification='c',
                     keep_on_top=True,
                     modal=True
                     )


def add_customer():
    print("Adding customer...")


def remove_customer_window():
    layout = [
        [sg.Text("Remove Customer", **h1)],
        [sg.Text("Which customer id do you want to remove?", font=("Helvetica", 12))],
        [sg.In(key='customer_id')],

        [sg.Button('Remove Customer'), sg.Button('Cancel')]
    ]

    return sg.Window('Remove customer', layout,
                     finalize=True,
                     size=(500, 400),
                     resizable=True,
                     element_justification='c',
                     keep_on_top=True,
                     modal=True
                     )


def remove_customer():
    selection = int(input("Which row do you want to remove?:"))
    data.pop(selection - 1)


def update_customer():
    print("updating customer")


def main():
    # Design pattern 1 - First window does not remain active
    # customer_screen = None
    # main_screen = make_window1()

    main_screen, customer_screen, order_screen, inventory_screen, add_customer_screen, remove_customer_screen = \
        frontpage_window(), None, None, None, None, None

    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WIN_CLOSED or None and window == main_screen:
            break

        if event == 'Customers' and not customer_screen:
            main_screen.hide()
            customer_screen = customer_window()

        if window == customer_screen and (event in (None, sg.WIN_CLOSED, 'Back')):
            customer_screen.close()
            customer_screen = None
            main_screen.un_hide()

        if window == customer_screen and (event in (sg.Button, 'Add Customer')):
            add_customer_window()
            customer_screen.close()
            customer_screen = customer_window()

        if window == customer_screen and (event in (sg.Button, 'Remove Customer')):
            remove_customer_window()
            customer_screen.close()
            customer_screen = customer_window()

        if window == customer_screen and (event in (sg.Button, 'Update Customer')):
            update_customer()
            customer_screen.close()
            customer_screen = customer_window()

        if event == 'Orders' and not order_screen:
            main_screen.hide()
            order_screen = order_window()

        if window == order_screen and (event in (None, sg.WIN_CLOSED, 'Back')):
            order_screen.close()
            order_screen = None
            main_screen.un_hide()

        if window == 'Inventory' and not inventory_screen:
            main_screen.hide()
            inventory_screen = inventory_window()

        if window == inventory_screen and (event in (None, sg.WIN_CLOSED, 'Back')):
            inventory_screen.close()
            inventory_screen = None
            main_screen.un_hide()

    main_screen.close()


if __name__ == '__main__':
    main()
