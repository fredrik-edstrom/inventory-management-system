import pandas as pd
from application.bll.controllers.customer_controller import *
from tabulate import tabulate

order = ['customer_id', 'company_name', 'first_name', 'last_name', 'address', 'zip_code', 'city', 'phone', 'email']


def main():
    print('Welcome to Rip and Ship!')
    print()

    while True:
        command = input('What would you like to do? : ')  # [['show'], ['Customers']]
        command = command.lower().split()

        if len(command) != 0:
            if command[0] in ['show', 'display', 'see', 'view']:
                data = get_all_customer()
                data = pd.DataFrame(data)
                data = data[order]
                print(tabulate(data, headers='keys', tablefmt='github', showindex=False))

            elif command[0] in ['add', 'create']:
                if len(command) > 1:
                    if command[1] in ['customers', 'customer', 'person', 'persons']:

                        customer = []
                        for item in order:
                            i = input(item)
                            customer.append(i)
                        z = zip(order, customer)
                        customer = dict(z)
                        create_customer(customer)

            if command[0] in ['remove', 'delete', 'drop', 'cancel', 'erase']:
                _id = int(input('Please enter the Customer_id you want to remove: '))
                remove_customer(_id)
                print(f'Deleted customer {_id}')

            elif command[0] in ['quit', 'exit']:
                print('Thanks for using Rip and Ship :)')
                break
        else:
            print("I can't do that yet :(")


if __name__ == '__main__':
    main()
