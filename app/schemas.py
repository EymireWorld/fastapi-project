from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Schema(BaseModel):
    model_config = ConfigDict(from_attributes= True)


class Scope(StrEnum):
    user = 'user'
    admin = 'admin'
    system = 'system'


class UserSchema(Schema):
    id: int
    username: str = Field(min_length=4, max_length=32)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr
    hashed_password: bytes
    created_at: datetime
    scope: Scope


class UserShowSchema(Schema):
    id: int = Field(min_length=4, max_length=32)
    username: str
    created_at: datetime


# =========================


class TaskSchema(Schema):
    id: int
    user_id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime


class TaskShowSchema(Schema):
    id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime
