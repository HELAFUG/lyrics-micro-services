from fastapi import APIRouter
from core.config import settings
from .external import external_router


api_router = APIRouter(
    prefix=settings.api.prefix,
    tags=["API"],
    responses={404: {"description": "Not found"}},
)

api_router.include_router(external_router)
