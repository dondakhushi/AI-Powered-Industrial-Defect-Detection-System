import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["defect_detection"]

print("Connected successfully!")
print("Databases visible:", client.list_database_names())