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
    # year_from: int = Field(ge=1900)
    # year_to: int = Field(le=2025)


    @field_validator("name")
    @classmethod
    def genre_compair(cls, v: str) -> str:
        with open("genres.json", "r") as f:
            data = json.load(f)
            valid_genres=[item['name'] for item in data]
        if v not in valid_genres:
            raise ValueError(f'Please enter a valid genre. \n Unknown genre: {v}')
        return v


def main():
    test= Year_genre_flow(name="Action")
    print(test)

if __name__ == '__main__':
    main()

















