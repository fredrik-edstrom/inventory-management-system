import datetime
import random

from application.bll.controllers import employee_controller, office_controller, \
    customer_cars_controller, contact_persons_controller, manufacturers_controller, orders_controller, \
    orderdetails_controller, product_controller, products_fit_models_controller, orders_from_manufacturers_controller, \
    orders_from_suppliers_controller, storages_controller, suppliers_controller, suppliers_orders_from_controller, \
    customer_controller
from generator.json_to_list import customers, employees, offices, cars, contact_persons, manufacturers, suppliers, products


def generate_order_dates(start, end):
    start_year, start_month, start_day = start.split('-')
    end_year, end_month, end_day = end.split('-')

    start = datetime.datetime(int(start_year), int(start_month), int(start_day))
    end = datetime.datetime(int(end_year), int(end_month), int(end_day))
    dates = []
    delivery = []

    for i in range(500):
        time_between_dates = end - start
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        dates.append(start + datetime.timedelta(days=random_number_of_days, hours=random.randrange(0, 12)
                                                , minutes=random.randrange(0, 60), seconds=random.randrange(0, 60)))

        delivery.append(dates[i] + datetime.timedelta(days=dates[i].day + 5 if dates[i].day + 5 < 28 else 5,
                                                      hours=dates[i].hour, minutes=dates[i].minute,
                                                      seconds=dates[i].second))

    return dates, delivery


def generate_cars():
    # for i in range 1 #range(len(cars)):
        car = {
            'vin_no': cars[i]['vin_no'],
            'customer_id': random.randrange(1, len(customers)),
            'color': cars[i]['color'],
            'year': cars[i]['year'],
            'model': cars[i]['model'],
            'brand': cars[i]['brand']
        }
        customer_cars_controller.create_customer_car(car)


def generate_customers():
    for i in range(len(customers)):
        customer = {
            'company_name': customers[i]['company_name'],
            'first_name': customers[i]['first_name'],
            'last_name': customers[i]['last_name'],
            'address': customers[i]['address'],
            'city': customers[i]['city'],
            'zip_code': customers[i]['zip_code'],
            'phone': customers[i]['phone'],
            'email': customers[i]['email']
        }
        customer_controller.create_customer(customer)


def generate_contact_persons():
    for i in range(len(contact_persons)):
        contact_person = {
            'first_name': contact_persons[i]['first_name'],
            'last_name': contact_persons[i]['last_name'],
            'email': contact_persons[i]['email'],
            'phone': contact_persons[i]['phone'],
        }
        contact_persons_controller.create_contact_person(contact_person)


def generate_employees():
    for i in range(len(employees)):
        employee = {
            'first_name': employees[i]['first_name'],
            'last_name': employees[i]['last_name'],
            'phone': employees[i]['phone'],
            'email': employees[i]['email'],
            'store_id': random.randrange(1, len(offices))
        }
        employee_controller.create_employee(employee)


def generate_manufacturers():
    for i in range(len(manufacturers)):
        manufacturer = {
            'company_name': manufacturers[i]['company_name'],
            'address': manufacturers[i]['address'],
            'city': manufacturers[i]['city'],
            'zip_code': manufacturers[i]['zip_code'],
            'contact_id': random.randrange(1, len(contact_persons))
        }
        manufacturers_controller.create_manufacturer(manufacturer)


def generate_offices():
    for i in range(len(offices)):
        office = {
            'name': offices[i]['name'],
            'address': offices[i]['address'],
            'zip_code': offices[i]['zip_code'],
            'phone': offices[i]['phone']
        }
        office_controller.create_office(office)


def generate_order_details():
    x = product_controller.get_all_product()
    x = [i for i in x]
    x = [str(i).split(',') for i in x]


    for i in range(500):
        y = random.choice(x)
        details = {
            'order_id': random.randrange(1, 500),
            'product_id': int(y[0]),
            'quantity': random.randrange(1, 50),
            'price_each': int(int(y[1]) * 1.5)
        }
        orderdetails_controller.create_orderdetails(details)


def generate_orders():
    dates, delivery = generate_order_dates('2000-01-01', '2022-01-01')

    for i in range(len(dates)):
        order = {
            'order_date': dates[i],
            'delivery_date': delivery[i],
            'customer_id': random.randrange(1, len(customers)),
            'employee_id': random.randrange(1, len(customers)),
        }
        orders_controller.create_orders(order)


def generate_products():
    for i in range(len(products)):
        product = {
            'product_name': products[i]['product_name'],
            'description': products[i]['description'],
            'price_in': products[i]['price_in'],
        }
        product_controller.create_product(product)


def generate_product_fits_models():
    for i in range(len(products) * 2):
        compatible = {
            'product_id': random.randrange(1, len(products)),
            'vin_no': cars[random.randrange(1, len(cars))]['vin_no']
        }
        products_fit_models_controller.create_products_fit_models(compatible)


def generate_orders_from_manufacturers():
    for i in range(len(products)):
        manufacturer_product = {
            'manufacturer_id': random.randrange(1, len(manufacturers)),
            'product_id': random.randrange(1, len(products))
        }
        orders_from_manufacturers_controller.create_orders_from_manufacturers(manufacturer_product)


def generate_orders_from_suppliers():
    for i in range(len(products)):
        supplier_product = {
            'supplier_id': random.randrange(1, len(suppliers)),
            'product_id': random.randrange(1, len(products))
        }
        orders_from_suppliers_controller.create_orders_from_suppliers(supplier_product)


def generate_storages():
    x = product_controller.get_all_product()
    x = [i for i in x]
    x = [str(i).split(',') for i in x]

    for i in range(500):
        y = random.choice(x)

        units = random.randrange(0, 100)
        storage = {
            'units_in_stock': units,
            'capacity': random.randrange(units, units + 100),
            'TRIGGERS': '404 NOT FOUND',
            'product_id': int(y[0])
        }
        storages_controller.create_storages(storage)


def generate_suppliers():
    for i in range(len(suppliers)):
        supplier = {
            'company_name': suppliers[i]['company_name'],
            'address': suppliers[i]['address'],
            'city': suppliers[i]['city'],
            'zip_code': suppliers[i]['zip_code'],
            'contact_id': random.randrange(1, len(contact_persons))
        }
        suppliers_controller.create_suppliers(supplier)


def generate_suppliers_orders_from():
    for i in range(len(suppliers)):
        orders_from = {
            'manufacturer_id': random.randrange(1, len(manufacturers)),
            'supplier_id': random.randrange(1, len(suppliers))
        }
        suppliers_orders_from_controller.create_suppliers_orders_from(orders_from)


def main():
    
    generate_cars()


if __name__ == '__main__':
    main()