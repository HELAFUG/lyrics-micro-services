from fastapi import APIRouter
from .users import users_router

external_router = APIRouter(prefix="/service-api")
external_router.include_router(users_router)
