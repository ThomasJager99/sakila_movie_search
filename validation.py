import pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import AliasChoices
from pydantic import ValidationError
from pydantic import ConfigDict
from pydantic import field_validator
from config import _mysql_conn
from pymysql import cursors
import json
from pydantic import StrictStr


# ====================================================================================================
#NOTE: trying to fetchall genres from my database to understand better validation method
# def genre_list():
#     sql='''SELECT category_id, name FROM category ORDER BY name;'''
#     with _mysql_conn() as conn, conn.cursor() as cur:
#         cur.execute(sql),
#         rows= cur.fetchall()
#     return json.dumps(rows, indent=4)
# print(genre_list())
#====================================================================================================
#NOTE: exported all genres to .json file in order to create own little db so i dont need to use conn
# for validation system every time and can use this genres like recomendation for user
# def genre_list(filename="genres.json"):
#     sql= '''  SELECT c.category_id, c.name, MIN(f.release_year) AS first_year, MAX(f.release_year) AS last_year
#         FROM category AS c
#         JOIN film_category AS fc ON fc.category_id = c.category_id
#         JOIN film AS f ON f.film_id = fc.film_id
#         GROUP BY c.category_id, c.name
#         ORDER BY c.name;
#          '''
#     with _mysql_conn() as conn, conn.cursor() as cur:
#         cur.execute(sql)
#         rows = list(cur.fetchall())
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(rows, f, indent=4, ensure_ascii=False)
#     print(f"Exported {len(rows)} genres to {filename}")
#====================================================================================================



class Keyword_search(BaseModel):
    model_config = ConfigDict(
        strict=True,                  #only strict types without conv
        validate_assignment=True,     #validation every new query
        str_strip_whitespace=True,    #auto-strip space
        str_min_length=1,
        str_max_length=10
    )

    keyword: StrictStr

    @field_validator("keyword")
    @classmethod
    def vali_keyword(cls, v: str) -> str:
        if not v.isalpha():
            raise ValueError("Keyword must contain only letters A-Z")
        return v









# class Key_word_validation(BaseModel):
#     model_config = ConfigDict(
#         str_min_length=1,
#         str_max_length=12,
#         validate_assignment=True
#     )
#
#     keyword: str
#
#     @field_validator("keyword")
#     @classmethod
#     def only_letters(cls, v: str) -> str:
#         v = v.strip()
#         if not v.isalpha():
#             raise ValueError("Keyword must be only letters")
#         return v
#
#
# # Key_word_validation(keyword=1)
#
# def main():
#     print("Running validation test")
#     try:
#         test = Key_word_validation(keyword='')
#         print(test)
#     except ValidationError as e:
#         for err in e.errors():
#             loc = ".".join(map(str, err["loc"]))
#             print(f"[invalid] {loc}: {err['msg']}")

# if __name__ == "__main__":
#     # genre_list()
#     main()






















