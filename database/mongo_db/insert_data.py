from database.mongo_db import mongo_db
from datetime import datetime


client = mongo_db.get_database()
db = client['message']


def store_session(speaker, text):
    # Access collection of the database

    collection1 = db['table1']

    conversation = {
        'speaker': speaker,
        'text': text,
        'datetime': datetime.now()
    }
    print(conversation)
    collection1.insert_one(conversation)