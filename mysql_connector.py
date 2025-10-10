import os
import pymysql
from dotenv import load_dotenv
from pymysql.cursors import DictCursor
from config import _mysql_conn

_conn=_mysql_conn()

#FIXME: Now we achieve connection through the config file and not at manual _conn function, but now
# i have a problem, connection closes immediately after 1 try so we need adjust pagination to new method.
#IDEA: Create loop while for stop this closing connection

# load_dotenv()
#Create connection to MySQL Database and transform output from tuples in dictionaries,
#and also put connection time in 5 seconds, .
# second all i make encapsulation for this function to hide it from another modules.
# def _conn():
#     return pymysql.connect(
#         host=os.getenv("MYSQL_HOST"),
#         port=int(os.getenv("MYSQL_PORT")),
#         user=os.getenv("MYSQL_USER"),
#         password=os.getenv("MYSQL_PASSWORD"),
#         database=os.getenv("MYSQL_DB"),
#         cursorclass=DictCursor,
#         autocommit=True,
#         connect_timeout=5,
#     )


#1st - List of Genres. Put all _conn function inside conn variable and force it to use SQL query and
#pull out a list with genres.
def list_of_genres():
    sql="SELECT category_id, name FROM category ORDER BY name;"
    with _conn as conn, conn.cursor() as cur:
        cur.execute(sql)
        return list(cur.fetchall())

#2.Min and max year in search.
#Simple ask from DB max and min. Wrap it integer and display it.
def years_bounds():
    sql="SELECT MIN(release_year) AS min_year, MAX(release_year) AS max_year FROM film;"
    with _conn as conn, conn.cursor() as cur:
        cur.execute(sql)
        row = cur.fetchone()
        if row:
            return int(row["min_year"]), int(row["max_year"])
        return None, None

#3.Keyword search.
#Create a query using %s like placeholders for future variable values, so it can
#easily replace them in future with input. %{keyword}% - will go in placeholder to
#LIKE and from MYSQL its "find anything after A% or what contains %ace%".
def search_by_keyword(keyword: str, limit=10, offset=0):
    sql= """
        SELECT film_id, title, release_year
        FROM film
        WHERE title LIKE %s
        ORDER BY title
        LIMIT %s OFFSET %s;
    """
    with _conn as conn, conn.cursor() as cur:
        cur.execute(sql, ((f"%{keyword}%"), int(limit), int(offset)))
        return list(cur.fetchall())

#4. Search by genre and year.
#Almost the same procedure as in previous search by keyword only with couple
#of more variables.
def search_by_genre_year(genre: str, y_from: int, y_to: int, limit=10, offset=0):
     sql= """
        SELECT f.film_id, f.title, f.release_year, c.name AS category
        FROM film AS f
        JOIN film_category AS fc ON fc.film_id = f.film_id
        JOIN category AS c ON c.category_id = fc.category_id
        WHERE c.name = %s
          AND f.release_year BETWEEN %s AND %s
        ORDER BY f.title
        LIMIT %s OFFSET %s;
    """
     with _conn as conn, conn.cursor() as cur:
         cur.execute(sql, (genre, int(y_from), int(y_to), int(limit), int(offset)))
         return list(cur.fetchall())






#Simple test.
# if __name__ == "__main__":
#     print("Genres:", list_of_genres()[:5])
#     print("Year bounds:", years_bounds())
#     print("Keyword 'ace':", search_by_keyword("ace", limit=5))
#     print("Genre+Years:", search_by_genre_year("Action", 2000, 2006, limit=5))

# Little test.
if __name__ == "__main__":
    from pprint import pprint
    try:
        bounds = years_bounds()
        print("Year bounds:", bounds)
    except Exception as e:
        print("ERROR:", e)




