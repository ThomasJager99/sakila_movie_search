from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
coll = db[os.getenv("MONGO_COLLECTION")]

resource = coll.insert_one({"_kind": "connect_test"})
print("Mongo PK, inserted id:", resource.inserted_id)










