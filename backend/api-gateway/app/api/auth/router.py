from typing import Annotated
from fastapi import APIRouter
from core.schemas.user import UserCreate, UserRead
from service.http import register_new_user

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register", response_model=UserRead)
async def register(user: UserCreate):
    return await register_new_user(user=user)
