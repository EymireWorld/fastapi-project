from fastapi import APIRouter, Query, status

from app.dependencies import session_dep, current_user_dep
from app.schemas import TaskShowSchema

from . import services
from .schemas import TaskCreateSchema, TaskUpdateSchema


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.get('')
async def get_tasks(
    session: session_dep,
    current_user: current_user_dep,
    limit: int = Query(10, ge=5, le=100),
    offset: int = Query(0, ge=0)
) -> list[TaskShowSchema] | None:
    return await services.get_tasks(session, current_user.id, limit, offset)


@router.get('/{task_id}')
async def get_task(
    session: session_dep,
    current_user: current_user_dep,
    task_id: int
) -> TaskShowSchema | None:
    return await services.get_task(session, current_user.id, task_id)


@router.post('')
async def create_task(
    session: session_dep,
    current_user: current_user_dep,
    data: TaskCreateSchema
) -> TaskShowSchema:
    return await services.create_task(session, current_user.id, data)


@router.put(
    '/{task_id}',
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
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(
    session: session_dep,
    current_user: current_user_dep,
    task_id: int
):
    await services.delete_task(session, current_user.id, task_id)
