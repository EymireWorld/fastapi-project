from datetime import datetime

from pydantic import EmailStr, Field

from app.schemas import Schema


class TokenSchema(Schema):
    access_token: str
    token_type: str


class UserSingUpSchema(Schema):
    username: str = Field(min_length=4, max_length=32)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)


class UserSingInSchema(Schema):
    username: str = Field(min_length=4, max_length=32)
    password: str = Field(min_length=8, max_length=64)


class UserProfileSchema(Schema):
    id: int
    username: str = Field(min_length=4, max_length=32)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr
    created_at: datetime
