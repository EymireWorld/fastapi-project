from fastapi import APIRouter, Query, status

from app.dependencies import current_user_dep, session_dep
from app.schemas import TaskDetailSchema, TaskSchema, TaskShortSchema

from . import services
from .schemas import TaskCreateSchema, TaskUpdateSchema


router = APIRouter()


@router.get(
    '',
    tags=['Tasks']
)
async def get_tasks(
    session: session_dep,
    limit: int = Query(10, ge=5, le=100),
    offset: int = Query(0, ge=0),
    is_completed: bool | None = Query(None)
) -> list[TaskShortSchema] | None:
    return await services.get_tasks(session, limit, offset, is_completed)


@router.get(
    '/{task_id}',
    tags=['Tasks']
)
async def get_task(
    session: session_dep,
    task_id: int
) -> TaskDetailSchema | None:
    return await services.get_task(session, task_id)


@router.post(
    '',
    tags=['Tasks'],
    status_code=status.HTTP_201_CREATED
)
async def create_task(
    session: session_dep,
    current_user: current_user_dep,
    data: TaskCreateSchema
) -> TaskSchema:
    return await services.create_task(session, current_user.id, data)


@router.put(
    '/{task_id}',
    tags=['Tasks'],
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_task(
    session: session_dep,
    current_user: current_user_dep,
    task_id: int,
    data: TaskUpdateSchema
):
    await services.update_task(session, current_user.id, task_id, data)



@router.delete(
    '/{task_id}',
    tags=['Tasks'],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(
    session: session_dep,
    current_user: current_user_dep,
    task_id: int
):
    await services.delete_task(session, current_user.id, task_id)
