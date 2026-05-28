import json

with open('data_files/cars.json', 'r', encoding='utf-8') as file:
    cars = json.load(file)

with open('data_files/contact_persons.json', 'r', encoding='utf-8') as file:
    contact_persons = json.load(file)

with open('data_files/customers.json', 'r', encoding='utf-8') as file:
    customers = json.load(file)

with open('data_files/employees.json', 'r', encoding='utf-8') as file:
    employees = json.load(file)

with open('data_files/manufacturers.json', 'r', encoding='utf-8') as file:
    manufacturers = json.load(file)

with open('data_files/products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

with open('data_files/offices.json', 'r', encoding='utf-8') as file:
    offices = json.load(file)

with open('data_files/suppliers.json', 'r', encoding='utf-8') as file:
    suppliers = json.load(file)
