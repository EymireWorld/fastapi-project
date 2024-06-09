from datetime import datetime, timezone

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TaskModel

from .schemas import TaskCreateSchema


async def get_tasks(session: AsyncSession, limit: int, offset: int):
    stmt = select(TaskModel)
    result = await session.execute(stmt)
    
    return result.scalars().all()[offset:][:limit]


async def get_task(session: AsyncSession, task_id: int):
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    result = await session.execute(stmt)
    
    return result.scalar()


async def create_task(session: AsyncSession, data: TaskCreateSchema, user_id: int):
    stmt = insert(TaskModel).values(
        user_id= user_id,
        title= data.title,
        description= data.description,
        is_completed= False,
        created_at= datetime.now(timezone.utc)
    )
    await session.execute(stmt)
    await session.commit()


async def update_task(session: AsyncSession, task_id: int, data: dict):
    pass


async def delete_task(session: AsyncSession, task_id: int):
    stmt = delete(TaskModel).where(TaskModel.id == task_id)
    await session.execute(stmt)
    await session.commit()
