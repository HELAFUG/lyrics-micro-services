from fastapi import APIRouter
from pydantic import EmailStr

"service-api/check_user_exist"

users_router = APIRouter(prefix="/users")


@users_router.get("/check_exist_user/{email}")
async def check_exist_user(email: EmailStr):
    return {"email": email}
