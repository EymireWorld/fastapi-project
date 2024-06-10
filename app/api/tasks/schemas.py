from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    title: str
    description: str | None = None


class TaskUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
