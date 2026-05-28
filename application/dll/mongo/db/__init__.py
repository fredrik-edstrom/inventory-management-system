from pymongo import MongoClient
from application.config.mongodb_config import *

client = MongoClient(f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?authSource=admin')
db = client.RipAndShipDB

# client.RipAndShipDB.command(
#  'createUser', USERNAME,
#  pwd=PASSWORD,
#  roles=[{'role': 'readWrite', 'db': DATABASE}]


