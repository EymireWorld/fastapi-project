from fastapi import APIRouter, Query

from app.dependencies import session_dep
from app.schemas import TaskShortSchema, UserDetailSchema, UserShortSchema

from . import services


router = APIRouter()

@router.get(
    '',
    tags=['Users']
)
async def get_users(
    session: session_dep,
    limit: int = Query(10, ge=5, le=100),
    offset: int = Query(0, ge=0)
) -> list[UserShortSchema] | None:
    return await services.get_users(session, limit, offset)


@router.get(
    '/{user_id}',
    tags=['Users']
)
async def get_user(
    session: session_dep,
    user_id: int
) -> UserDetailSchema | None:
    return await services.get_user(session, user_id)


@router.get(
    '/{user_id}/tasks',
    tags=['Users', 'Tasks']
)
async def get_user(
    session: session_dep,
    user_id: int,
    limit: int = Query(10, ge=5, le=100),
    offset: int = Query(0, ge=0),
    is_completed: bool | None = Query(None)
) -> list[TaskShortSchema] | None:
    return await services.get_user_tasks(session, user_id, limit, offset, is_completed)
