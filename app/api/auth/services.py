from fastapi import HTTPException, status
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import UserModel

from .dependencies import encode_jwt, hash_password, validate_password
from .schemas import TokenSchema, UserSingInSchema, UserSingUpSchema


async def sing_in(
    session: AsyncSession,
    data: UserSingInSchema
):
    stmt = select(UserModel).where(UserModel.username == data.username)
    result = await session.execute(stmt)
    result = result.scalar()

    if (not result) and (not validate_password(data.password, result.hashed_password)):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= 'Invalid username or password.'
        )
    if not result.is_active:
        raise HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= 'User inactive.'
    )

    return TokenSchema(
        access_token= encode_jwt(result.id),
        token_type= 'Bearer'
    )


async def sing_up(
    session: AsyncSession,
    data: UserSingUpSchema
):
    values = {
        'username': data.username,
        'first_name': data.first_name,
        'last_name': data.last_name,
        'email': data.email,
        'hashed_password': hash_password(data.password)
    }
    stmt = insert(UserModel).values(**values).returning(UserModel.id)

    try:
        result = await session.execute(stmt)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail= 'Username or email is already registered.'
        )
    else:
        await session.commit()

    return TokenSchema(
        access_token= encode_jwt(result.scalar()),
        token_type= 'Bearer'
    )
