from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from repository.user import get_user_by_email


async def check_exist_user(session: AsyncSession, email: str):
    user = await get_user_by_email(session=session, email=email)
    if user:
        raise HTTPException(status_code=200, detail=True)

    return {"detail": False}
