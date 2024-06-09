from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    title: str
    description: str | None = None
