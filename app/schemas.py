from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    hashed_password: bytes
    created_at: datetime
    scope: str


class TaskSchema(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None = None
    is_completed: bool = False
    created_at: datetime
