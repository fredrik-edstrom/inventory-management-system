from main_menu import *
from customer_windows import *
from order_windows import *
from inventory_windows import *
from application.bll.controllers.customer_controller import *
from application.bll.controllers.storages_controller import *


'''
Main window for the GUI, containing the Event-handler-loop.
In order to run the GUI, run this file.

Variables = edit settings for the windows and buttons. (Fonts etc.)
'''



def event_handler():
    # Windows:
    main_screen, customer_screen, orders_screen, inventory_screen, \
        add_customer_screen, edit_customer_screen, place_order_screen,\
        edit_order_screen, place_int_order_screen, edit_int_order_screen, \
        update_item_screen, edit_item_screen, add_item_screen, search_cust_screen, search_item_screen = \
        main_menu(), None, None, None, None, None, None, None, None,None, None, None, None, None, None

    selected_row = None

# Event handler loop
    while True:
        # prepare all windows
        window, event, values = sg.read_all_windows()

# MAIN MENU SCREEN
        if event == sg.WIN_CLOSED or None and window == main_screen:
            break
        # Customers - button
        if event == 'Customers' and not customer_screen:
            main_screen.close()
            customer_screen = customer_window()
        # Orders - button
        if event == 'Orders' and not orders_screen:
            main_screen.close()
            orders_screen = orders_window()
        # Inventory - button
        if event == 'Inventory' and not inventory_screen:
            main_screen.close()
            inventory_screen = inventory_window()

# Customer Screen buttons
        if window == customer_screen:
            if event in '-TABLE-':
                selected_row = values['-TABLE-'][0]
                cid = (get_all_customer()[selected_row]['_id'])

            if event in (sg.Button, 'Back'):
                customer_screen.close()
                customer_screen = None
                main_screen = main_menu()

            if event in (sg.Button, 'Add Customer'):
                add_customer_screen = add_customer_window()

            if event in (sg.Button, 'Remove Customer') and selected_row is not None:
                remove_customer(cid)
                customer_screen.close()
                customer_screen = customer_window()

            if event in (sg.Button, 'Edit Customer') and selected_row is not None:
                edit_customer_screen = edit_customer_window()

            if event in (sg.Button, 'Search'):
                temp = ['Please choose search filter in the drop-down menu ...']
                search_cust_screen = search_cust_window(temp)

# SEARCH CUSTOMER
        if window == search_cust_screen:
            if event in (sg.Button, 'Search'):
                results = [[value for value in d.values()]
                           for d in search_for_customer(str(values['col']), str(values['value']))]
                search_cust_screen.close()
                search_cust_screen = search_cust_window(results)

            if event in (sg.Button, 'Cancel'):
                search_cust_screen.close()

#  ADD CUSTOMER SCREEN
        if window == add_customer_screen:
            # Add Customer
            if event in (sg.Button, '-ADD-'):
                create_customer(values)

                add_customer_screen.close()
                customer_screen.close()
                customer_screen = customer_window()
            # Cancel
            if event in (sg.Button, 'Cancel'):
                add_customer_screen.close()

# EDIT CUSTOMER WINDOW
        if window == edit_customer_screen:
            if event in (sg.Button, 'Submit'):
                col = values['col']
                value = values['value']
                update_customer(int(cid), str(col), str(value))

                edit_customer_screen.close()
                customer_screen.close()
                customer_screen = customer_window()

            if event in (sg.Button, 'Cancel'):
                edit_customer_screen.close()


# INVENTORY WINDOW
        if window == inventory_screen:
            if event in '-TABLE-':
                selected_row = values['-TABLE-'][0]
                row = (get_all_storages()[selected_row]['shelf_id'])

            if event in (sg.Button, 'Search'):
                search_item_screen = search_item_window(get_all_storages())

            if event in (sg.Button, "Back"):
                main_screen = main_menu()
                inventory_screen.close()
                inventory_screen = None

            if event in (sg.Button, 'Add item'):
                add_item_screen = add_item_window()

            if event in (sg.Button, 'Delete item') and selected_row is not None:
                remove_storage(row)
                inventory_screen.close()
                inventory_screen = inventory_window()

            if event in (sg.Button, 'Update item') and selected_row is not None:
                edit_item_screen = edit_item_window()

            if event in (sg.Button, 'Approve orders'):
                remove_temp_orders()
                print('Orders approved!')

            if event in (sg.Button, 'Delete order') and selected_row is not None:
                inventory_screen.close()
                inventory_screen = inventory_window()
# SEARCH ITEM
        if window == search_item_screen:
            if event in (sg.Button, 'Submit'):
                results = [[value for value in d.values()]
                           for d in search_for_storage(str(values['col']), str(values['value']))]
                search_item_screen.close()
                search_cust_screen = search_item_window(results)
# ADD ITEM
        if window == add_item_screen:
            if event in (sg.Button, '-ADD-'):
                create_storages(values)

                add_item_screen.close()
                add_item_screen = None

                inventory_screen.close()
                inventory_screen = inventory_window()
# EDIT ITEM
        if window == edit_item_screen:
            if event in (sg.Button, 'Submit'):
                col = values['col']
                value = values['value']

                update_storage(int(row), str(col), str(value))
            edit_item_screen.close()
            edit_item_screen = None

            inventory_screen.close()
            inventory_screen = inventory_window()


# ORDER WINDOW
        if window == orders_screen:
            if event in (sg.Button, "Back"):
                main_screen = main_menu()
                orders_screen.close()
                orders_screen = None

            if event in '-TABLE-':
                selected_row = values['-TABLE-'][0]

            if event in (sg.Button, 'Place order'):
                place_order_screen = place_order_window()

            if event in (sg.Button, 'Cancel order') and selected_row is not None:
                order_data.pop(selected_row)

                orders_screen.close()
                orders_screen = orders_window()

            if event in (sg.Button, 'Edit order') and selected_row is not None:
                edit_order_screen = edit_order_window(order_data[selected_row])

        # PLACE ORDER WINDOW
        if window == place_order_screen:
            if event in (sg.Button, '-PLACE-'):
                output = [str(values[key]) for key in values]
                place_order(output)

                place_order_screen.close()
                orders_screen.close()
                orders_screen = orders_window()

            # Cancel
            if event in (sg.Button, 'Cancel'):
                place_order_screen.close()

        if window == edit_order_screen:
            if event in (sg.Button, '-EDIT-'):
                output = [str(values[key]) for key in values]
                edit_order(selected_row, output)

                edit_order_screen.close()
                orders_screen.close()
                orders_screen = orders_window()

            if event in (sg.Button, 'Cancel'):
                edit_order_screen.close()



if __name__ == '__main__':
    event_handler()
