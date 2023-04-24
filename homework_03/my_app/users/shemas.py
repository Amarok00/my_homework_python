from pydantic import BaseModel, Field
from uuid import uuid4


class UserBase(BaseModel):
    username: str = Field(
        ...,
        example="john",
        min_length=3,
        max_length=20,
    )


class UserOut(UserBase):
    id: int = Field(..., example=123)


class UserIn(UserBase):
    ...


def generate_token():
    token = str(uuid4())
    print("New token:", token)
    return str()


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)
