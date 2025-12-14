from fastapi import APIRouter
from core.config import settings
from .users import users_router

external_router = APIRouter(
    prefix=settings.api.notify,
)

external_router.include_router(users_router)
