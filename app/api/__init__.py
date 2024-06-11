from fastapi import APIRouter

from .auth import router as auth_router
from .tasks import router as tasks_router
from .users import router as users_router


__all__ = ['router']


router = APIRouter(
    prefix='/api'
)

router.include_router(
    auth_router,
    prefix='/auth'
)
router.include_router(
    tasks_router,
    prefix='/tasks'
)
router.include_router(
    users_router,
    prefix='/users'
)