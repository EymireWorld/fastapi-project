from fastapi import APIRouter

from app.dependencies import current_user_dep, session_dep

from . import services
from .schemas import (
    TokenSchema,
    UserProfileSchema,
    UserSingInSchema,
    UserSingUpSchema
)


router = APIRouter(
    tags=['Auth']
)


@router.post('/sign_in')
async def sign_in(
    session: session_dep,
    data: UserSingInSchema
) -> TokenSchema:
    return await services.sing_in(session, data)


@router.post('/sign_up')
async def sign_up(
    session: session_dep,
    data: UserSingUpSchema
) -> TokenSchema:
    return await services.sing_up(session, data)


@router.get('/me')
async def profile(current_user: current_user_dep) -> UserProfileSchema:
    return current_user
