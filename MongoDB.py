#Author Benjamin Schäfer, ELias Tilegant

from http import client
from pymongo import MongoClient, InsertOne
import json
import tables


client = MongoClient("mongodb://localhost:27017")

db = client["DB2-1"]
users = db["user_data"]
collection = db["collection"]
requesting = []

def init(filepath):
    with open(filepath) as f:
        for jsonObj in f:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))

    result = collection.bulk_write(requesting)

def create():
    tables.countries.country_id = 10
    db.users.insert_one()

def read():
    db.users.find().limit()

def update():
    db.users.update_many()

def delete():
    db.users.delete_many({status : "reject"})