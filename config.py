import os
import pymysql.cursors
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

# Загружаем .env в переменные окружения
load_dotenv()

# MySQL settings
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB = os.getenv("MYSQL_DB", "sakila")

# MongoDB settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "logs_db")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "final_project_logs")

"________________MySQL Connection__________________"
def _mysql_conn():
    conn= pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        connect_timeout=5
    )
    return conn

"________________MongoDB Connection__________________"
_MONGO_CLIENT = MongoClient(os.getenv("MONGO_URI"))

def get_mongo_connect():
    db = _MONGO_CLIENT[os.getenv("MONGO_DB", "logs_db")]
    return db[os.getenv("MONGO_COLLECTION", "final_project_logs")]


