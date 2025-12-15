from fastapi import APIRouter
from core.config import settings
from fastapi import Response
from mailing.welcome import send_welcome_email
from .external import external_router


api_router = APIRouter(
    prefix=settings.api.prefix,
    tags=["API"],
    responses={404: {"description": "Not found"}},
)

api_router.include_router(external_router)


@api_router.post("/{email}")
async def send_test_email(email: str):
    await send_welcome_email(email)
    return Response(status_code=200)
