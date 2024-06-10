from fastapi import APIRouter

from app.dependencies import session_dep, current_user_dep

from . import services
from .schemas import TokenSchema, UserSingInSchema, UserSingUpSchema, UserProfileSchema


router = APIRouter(
    prefix='/auth',
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


@router.get('/me', response_model= UserProfileSchema)
async def profile(current_user: current_user_dep):
    return current_user
