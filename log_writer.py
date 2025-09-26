from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

#Single global connection to MongoDB------
#The big and core difference between Mongo connection amd MySQL is that MongoClient
#is the one and only connection, it maneged and hold inside several pulls, open and
#close them if its needed. In the MySQL we have to create, open and close it with context manager "with as"
_client=MongoClient(os.getenv("MONGO_URI"))
_db=MongoClient(os.getenv("MONGO_DB"))
_coll=MongoClient(os.getenv("MONGO_COLLECTION"))

#Single global connection to MongoDB------

#Filter - this function will test data
def _jsonable(obj):
    """Make params safely storable (e.g., convert sets, etc.)."""
    try:
        json.dumps(obj)
        return obj
    except TypeError:
        return json.loads(json.dumps(obj, default=str))




















