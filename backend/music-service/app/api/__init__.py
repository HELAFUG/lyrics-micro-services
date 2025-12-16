from fastapi import APIRouter
from core.config import settings
from api.author import author_router

api_router = APIRouter(prefix=settings.api.prefix)
api_router.include_router(router=author_router)
