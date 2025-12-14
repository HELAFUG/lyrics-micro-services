from fastapi import APIRouter, Response
from mailing.welcome import send_welcome_email, send_login_email

users_router = APIRouter(
    prefix="/users",
)


@users_router.post("/after-register/{user_email}")
async def after_register(user_email: str):
    await send_welcome_email(email=user_email)
    return Response(status_code=200)


@users_router.post("/after-login/{user_email}")
async def after_login(user_email: str):
    await send_login_email(email=user_email)
    return Response(status_code=200)
