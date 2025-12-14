from fastapi import APIRouter
from mailing.welcome import send_welcome_email

users_router = APIRouter(
    prefix="/users",
)


@users_router.post("/after-register/{user_email}")
async def after_register(user_email: str):
    await send_welcome_email(email=user_email)
