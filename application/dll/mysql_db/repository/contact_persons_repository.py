import re

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import ContactPerson


def create_contact_person(contact_person: dict):
    contact_person = ContactPerson(**contact_person)
    session.add(contact_person)
    session.commit()


def remove_contact_person(_id: int):
    contact_person = session.query(ContactPerson).filter(ContactPerson.contact_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_contact_person(_id: int, column: str, update: str):
    session.query(ContactPerson).filter(ContactPerson.contact_id == _id).update({column: update})
    session.commit()


def get_contact_person_by_id(_id: int) -> dict:
    contact_person = session.query(ContactPerson).filter(ContactPerson.contact_id == _id).first()
    return {i.name: getattr(contact_person, i.name) for i in contact_person.table.columns}


def order_by_contact_person(column: str) -> list:
    return [{
                'contact_id': contact_person.contact_id,
                'first_name': contact_person.first_name,
                'last_name': contact_person.last_name,
                'email': contact_person.email,
                'phone': contact_person.phone
            } for contact_person in session.query(ContactPerson).order_by(column)]


def search_for_contact_person(column: str, search_for: str) -> list:
    contact_person = session.query(ContactPerson).all()
    return [{
                'contact_id': contact_person.contact_id,
                'first_name': contact_person.first_name,
                'last_name': contact_person.last_name,
                'email': contact_person.email,
                'phone': contact_person.phone
            } for customer in contact_person if re.search(search_for, getattr(customer, column))]


def get_all_contact_persons() -> list:
    persons = session.query(ContactPerson).all()
    return [{i.name: getattr(person, i.name) for i in person.__table__.columns} for person in persons]
