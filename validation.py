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























