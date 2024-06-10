from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import UserModel


async def get_users(session: AsyncSession, limit: int, offset: int):
    stmt = select(UserModel)
    result = await session.execute(stmt)
    
    return result.scalars().all()[offset:][:limit]


async def get_user(session: AsyncSession, user_id: int):
    stmt = select(UserModel).where(UserModel.id == user_id)
    result = await session.execute(stmt)
    
    return result.scalar()
