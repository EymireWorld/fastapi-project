from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TaskModel, UserModel


async def get_users(
    session: AsyncSession,
    limit: int,
    offset: int
):
    stmt = select(UserModel).offset(offset).limit(limit)
    result = await session.execute(stmt)
    
    return result.scalars().all()


async def get_user(
    session: AsyncSession,
    user_id: int
):
    stmt = select(UserModel).where(UserModel.id == user_id)
    result = await session.execute(stmt)

    return result.scalar()


async def get_user_tasks(
    session: AsyncSession,
    user_id: int,
    limit: int,
    offset: int,
    is_completed: bool | None
):
    if is_completed == None:
        stmt = select(TaskModel).where(TaskModel.user_id == user_id).offset(offset).limit(limit)
    else:
        stmt = select(TaskModel).where(and_(
            TaskModel.user_id == user_id,
            TaskModel.is_completed == is_completed
        )).offset(offset).limit(limit)
    result = await session.execute(stmt)

    return result.scalars().all()
