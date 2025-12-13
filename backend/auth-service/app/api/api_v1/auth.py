from fastapi import APIRouter
from .fastapi_users import fastapi_users
from core.config import settings
from core.schemas.user import UserRead, UserCreate
from api.dependencies.authentication import authentication_backend

auth_router = APIRouter(prefix=settings.api_v1.auth)


auth_router.include_router(fastapi_users.get_auth_router(authentication_backend))

auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
