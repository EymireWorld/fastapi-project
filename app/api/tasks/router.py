from fastapi import APIRouter
from app.dependencies import session_dep
from app.schemas import TaskSchema as Task
from . import services


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.get('')
async def get_tasks(session: session_dep, limit: int = 10, offset: int = 0) -> list[Task] | None:
    return await services.get_tasks(session, limit, offset)


@router.get('/{task_id}')
async def get_task(session: session_dep, task_id: int) -> Task | None:
    return await services.get_task(session, task_id)


@router.post('')
async def create_task(session: session_dep):
    pass


@router.put('/{task_id}')
async def update_task(session: session_dep, task_id: int):
    pass



@router.delete('/{task_id}')
async def delete_task(session: session_dep, task_id: int):
    pass
