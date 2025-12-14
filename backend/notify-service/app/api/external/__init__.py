from fastapi import APIRouter
from core.config import settings

external_router = APIRouter(
    prefix=settings.api.notify,
)
