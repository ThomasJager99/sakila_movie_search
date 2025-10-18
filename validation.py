import pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import AliasChoices
from pydantic import ValidationError
from pydantic import ConfigDict
from pydantic import field_validator

class Key_word_validation(BaseModel):
    model_config = ConfigDict(
        str_min_length=1,
        str_max_length=12,
        validate_assignment=True
    )

    keyword: str

    @field_validator("keyword")
    @classmethod
    def only_letters(cls, v: str) -> str:
        v = v.strip()
        if not v.isalpha():
            raise ValueError("Keyword must be only letters")
        return v


# Key_word_validation(keyword=1)

def main():
    print("Running validation test")
    try:
        test = Key_word_validation(keyword='')
        print(test)
    except ValidationError as e:
        for err in e.errors():
            loc = ".".join(map(str, err["loc"]))
            print(f"[invalid] {loc}: {err['msg']}")

if __name__ == "__main__":
    main()






















