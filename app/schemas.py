from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Schema(BaseModel):
    model_config = ConfigDict(from_attributes= True)


class Scope(StrEnum):
    user = 'user'
    admin = 'admin'
    system = 'system'


# =========================


class UserSchema(Schema):
    id: int
    username: str = Field(min_length=4, max_length=32)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr
    hashed_password: bytes
    created_at: datetime
    scope: Scope


class UserShortSchema(Schema):
    id: int = Field(min_length=4, max_length=32)
    username: str
    created_at: datetime


class UserDetailSchema(Schema):
    id: int
    username: str = Field(min_length=4, max_length=32)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    created_at: datetime
    scope: Scope


# =========================


class TaskSchema(Schema):
    id: int
    user_id: int
    title: str = Field(max_length=64)
    description: str | None = Field(max_length=256)
    is_completed: bool
    created_at: datetime


class TaskShortSchema(Schema):
    id: int
    title: str = Field(max_length=64)
    is_completed: bool


class TaskDetailSchema(Schema):
    id: int
    user_id: int
    title: str = Field(max_length=64)
    description: str | None = Field(max_length=256)
    is_completed: bool
    created_at: datetime
