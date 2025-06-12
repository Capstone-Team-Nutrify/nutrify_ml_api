# import os
# from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()

# client = MongoClient(os.getenv("MONGO_URI"))
# db = client.get_default_database()
# collection = db["predict"]

# def save_predict_log(disease_rate_predict):
#     document_entry = {
#         "predict": disease_rate_predict
#     }
#     collection.insert_one(document_entry)

