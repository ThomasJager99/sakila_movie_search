from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
coll = db[os.getenv("MONGO_COLLECTION")]

resource = coll.insert_one({"_kind": "connect_test"})
print("Mongo PK, inserted id:", resource.inserted_id)


# import pymysql
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# def check_connection_mysql():
#     try:
#         conn = pymysql.connect(
#             host=os.getenv("MYSQL_HOST"),
#             port=int(os.getenv("MYSQL_PORT")),
#             user=os.getenv("MYSQL_USER"),
#             password=os.getenv("MYSQL_PASSWORD"),
#             database=os.getenv("MYSQL_DB")
#         )
#         print("MySQL connection established")
#         conn.close()
#         return True
#     except Exception as e:
#         print("Cannot establish connection to Database")
#         return False
#
# if __name__ == "__main__":
#     check_connection_mysql()

import pymysql
import os
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

load_dotenv()

def search_by_keyword(keyword, limit=10, offset=0):
    conn = None
    try:
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT")),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB"),
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cur:
            sql = """
                SELECT film_id, title, release_year
                FROM film
                WHERE title LIKE %s
                ORDER BY title
                LIMIT %s OFFSET %s
            """
            cur.execute(sql, (f"%{keyword}%", limit, offset))
            results = cur.fetchall()
            return results

    except Exception as e:
        print("Error", e)
        return []
    finally:
        if conn:
            conn.close()

# if __name__ == "__main__":
#     films = search_by_keyword("ace", limit=10, offset=0)
#     if films:
#         for f in films:
#             print(f"{f['film_id']}: {f['title']} ({f['release_year']})")
#         else:
#             print("Фильмы не найдены")












