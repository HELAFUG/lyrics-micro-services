from aiohttp import ClientSession
from core.config import settings
from fastapi import HTTPException


async def fetch_exist_user(email: str) -> bool:
    async with ClientSession() as session:
        async with session.get(
            f"{settings.external.auth.check_user_exist}?email={email}"
        ) as response:
            if response.json().get("detail") == True:
                return True
            return False
