from fastapi import APIRouter
from core.config import settings

profile_router = APIRouter(
    prefix=settings.api.v1.authors,
    tags=["Authors"],
)
