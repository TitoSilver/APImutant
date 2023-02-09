import os

from pymongo import MongoClient
from pymongo.database import Database

def get_mongo_database() -> Database:
    connection_str = os.environ.get("MONGO_CONNECTION_URL", "mongodb://localhost:27017/")
    db_name = os.environ.get("MONGO_DATABASE_NAME", "mongo_mutans")
    #port = os.environ.get('PORT',4200)

    mongo_client = MongoClient(connection_str, serverSelectionTimeoutMS=5)
    database = mongo_client.get_database(db_name)

    return database
