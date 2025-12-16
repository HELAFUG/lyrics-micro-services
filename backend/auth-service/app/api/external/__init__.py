from fastapi import APIRouter
from .users import users_router

external_router = APIRouter(
    prefix="/service-api", tags=["External API`s for Other Services"]
)
external_router.include_router(users_router)
