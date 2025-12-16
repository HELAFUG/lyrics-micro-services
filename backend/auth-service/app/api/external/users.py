from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from service.users import check_exist_user
from core.models import db_helper

"service-api/check_user_exist"

users_router = APIRouter(prefix="/users")


@users_router.get("/check_exist_user/{email}")
async def check_user_in_db(
    email: EmailStr,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await check_exist_user(session=session, email=email)
