import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def check_connection_mysql():
    try:
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT")),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
        print("MySQL connection established")
        conn.close()
        return True
    except Exception as e:
        print("Cannot establish connection to Database")
        return False

if __name__ == "__main__":
    check_connection_mysql()












