from datetime import datetime, timezone

from sqlalchemy import and_, delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TaskModel

from .schemas import TaskCreateSchema, TaskUpdateSchema


async def get_tasks(session: AsyncSession, user_id: int, limit: int, offset: int):
    stmt = select(TaskModel).where(TaskModel.user_id == user_id)
    result = await session.execute(stmt)
    
    return result.scalars().all()[offset:][:limit]


async def get_task(session: AsyncSession, user_id: int, task_id: int):
    stmt = select(TaskModel).where(and_(
        TaskModel.id == task_id,
        TaskModel.user_id == user_id
    ))
    result = await session.execute(stmt)
    
    return result.scalar()


async def create_task(session: AsyncSession, user_id: int, data: TaskCreateSchema):
    stmt = insert(TaskModel).values(
        user_id= user_id,
        title= data.title,
        description= data.description,
        is_completed= False,
        created_at= datetime.now(timezone.utc)
    ).returning(TaskModel)
    result = await session.execute(stmt)
    await session.commit()

    return result


async def update_task(session: AsyncSession, user_id: int, task_id: int, data: TaskUpdateSchema):
    stmt = update(TaskModel).where(and_(
        TaskModel.id == task_id,
        TaskModel.user_id == user_id
    )).values(**data.model_dump(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()


async def delete_task(session: AsyncSession, user_id: int, task_id: int):
    stmt = delete(TaskModel).where(and_(
        TaskModel.id == task_id,
        TaskModel.user_id == user_id
    ))
    await session.execute(stmt)
    await session.commit()
