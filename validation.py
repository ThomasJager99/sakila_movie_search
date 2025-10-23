import pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import AliasChoices
from pydantic import ValidationError
from pydantic import ConfigDict
from pydantic import field_validator
from pydantic import model_validator
from config import _mysql_conn
from pymysql import cursors
import json
from pydantic import StrictStr
from genres_repo import load_genres_map

#======First One Validator for Keyword=======
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
#===============================================================================================
#NOTE: Second one, Validator for genre and year.
#===============================================================================================

class Year_genre_flow(BaseModel):
    model_config = ConfigDict(
        strict=True,
        validate_assignment=True,
        str_strip_whitespace=True,
        str_max_length=10,
        str_min_length=1
    )

    name: StrictStr
    year_from: int = Field(ge=1990, le=2025)
    year_to: int = Field(ge=1990, le=2025)

#NOTE: This one validate only str field, and contain inside connection to cached data from genre.json
# in more useful format of dict and compare it faster with users input.
    @field_validator("name")
    @classmethod
    def genre_compair(cls, v: str) -> str:
        v_norm = v.strip()
        genres = load_genres_map()
        key= v_norm.casefold()
        if key not in genres:
            raise ValueError(f'Please enter a valid genre. \nUnknown genre: {v}')
        return v_norm

#NOTE: This func is currently wirking with self models what we already create
# And its validate possible logical error with two different year fields.
    @model_validator(mode='after')
    def year_compair(self):
        if self.year_from > self.year_to:
            raise ValueError(f'Left bound {self.year_from} must be less then Right bound {self.year_to}')
        return self


# def main():
#     try:
#         test= Year_genre_flow(name="AcTiOn", year_from=1980, year_to=2010)
#         print(test)
#     except ValidationError as f:
#         print(f'Wrong type of object {f}')
#
# if __name__ == '__main__':
#     main()



# def test_main():
#     try:
#         test= Year_genre_flow(name="AcTiOn", year_from=2005, year_to=2010)
#         print(test)
#     except ValidationError as f:
#         print(f'Wrong type of object {f}')

