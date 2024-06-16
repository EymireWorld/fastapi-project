from pydantic import Field
from app.schemas import Schema


class TaskCreateSchema(Schema):
    title: str = Field(max_length=64)
    description: str | None = Field(None, max_length=256)


class TaskUpdateSchema(Schema):
    title: str | None = Field(None, max_length=64)
    description: str | None = Field(None, max_length=256)
    is_completed: bool | None = None
