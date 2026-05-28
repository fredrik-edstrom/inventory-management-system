import time
from application.bll.controllers.customer_controller import search_for_customer


def main():
    t1 = time.time()
    customer_dicts = search_for_customer('first_name', 'ma')
    print(customer_dicts)
    t2 = time.time()
    timer = t2 - t1
    print(timer)


if __name__ == '__main__':
    main()
