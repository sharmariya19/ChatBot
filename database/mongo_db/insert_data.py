from database.mongo_db import mongo_db
from datetime import datetime


client = mongo_db.get_database()
db = client['chatbot']


def store_session(name, speaker, text):
    # Access collection of the database

    collection1 = db[name]

    conversation = {
        'speaker': speaker,
        'text': text,
        'datetime': datetime.now()
    }
    collection1.insert_one(conversation)