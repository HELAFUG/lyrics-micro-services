from fastapi import HTTPException
from repository.user import get_user_by_email


async def check_exist_user(email: str):
    user = await get_user_by_email(email=email)
    if user:
        raise HTTPException(status_code=200, detail={"user_exist_in_db": True})

    return {"user_exist_in_db": False}
