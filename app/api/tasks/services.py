from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TaskModel

from .schemas import TaskCreateSchema, TaskUpdateSchema


async def get_tasks(
    session: AsyncSession,
    limit: int,
    offset: int,
    is_completed: bool | None
):
    if is_completed == None:
        stmt = select(TaskModel).offset(offset).limit(limit)
    else:
        stmt = select(TaskModel).where(TaskModel.is_completed == is_completed).offset(offset).limit(limit)
    result = await session.execute(stmt)

    return result.scalars().all()


async def get_task(
    session: AsyncSession,
    task_id: int
):
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    result = await session.execute(stmt)
    result = result.scalar()
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found.'
        )

    return result


async def create_task(
    session: AsyncSession,
    user_id: int,
    data: TaskCreateSchema
):
    stmt = insert(TaskModel).values(
        user_id= user_id,
        title= data.title,
        description= data.description,
        is_completed= False,
        created_at= datetime.now(timezone.utc)
    ).returning(TaskModel)
    result = await session.execute(stmt)
    await session.commit()

    return result.scalar()


async def update_task(
    session: AsyncSession,
    user_id: int,
    task_id: int,
    data: TaskUpdateSchema
):
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    result = await session.execute(stmt)
    result = result.scalar()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found.'
        )
    elif result.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Access Denied.'
        )

    stmt = update(TaskModel).where(TaskModel.id == task_id).values(**data.model_dump(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()


async def delete_task(
    session: AsyncSession,
    user_id: int,
    task_id: int
):
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    result = await session.execute(stmt)
    result = result.scalar()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found.'
        )
    elif result.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Access Denied.'
        )

    stmt = delete(TaskModel).where(TaskModel.id == task_id)
    await session.execute(stmt)
    await session.commit()
