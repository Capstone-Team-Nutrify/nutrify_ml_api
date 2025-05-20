import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_default_database()
collection = db["history"]

def save_predict_log(input_makanan, disease_rate_predict):
    document_entry = {
        "makanan": input_makanan,
        "disease_rate": disease_rate_predict
    }
    collection.insert_one(document_entry)

