from typing import Annotated
from fastapi import APIRouter
from core.schemas.user import UserCreate, UserRead
from service.http import register_new_user, login_exist_user

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    "/register",
)
async def register(user: UserCreate):
    return await register_new_user(user=user)


@auth_router.post("/login")
async def login(user: UserCreate):
    return await login_exist_user(user=user)
