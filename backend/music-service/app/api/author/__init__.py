from fastapi import APIRouter
from core.config import settings
from .router import router

author_router = APIRouter(
    prefix=settings.api.v1.authors,
    tags=["Authors"],
)

author_router.include_router(router=router)
