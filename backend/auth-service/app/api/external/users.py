from fastapi import APIRouter
from pydantic import EmailStr
from service.users import check_exist_user

"service-api/check_user_exist"

users_router = APIRouter(prefix="/users")


@users_router.get("/check_exist_user/{email}")
async def check_user_in_db(email: EmailStr):
    return await check_exist_user(email=email)
