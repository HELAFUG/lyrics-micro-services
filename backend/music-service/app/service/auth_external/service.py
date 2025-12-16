from aiohttp import ClientSession
from core.config import settings
from fastapi import HTTPException


async def fetch_exist_user(email: str) -> bool:
    async with ClientSession() as session:
        async with session.get(
            f"{settings.external.auth.check_user_exist}/{email}"
        ) as response:
            resp_dict = await response.json()
            if response.status != 200:
                raise HTTPException(
                    status_code=response.status,
                    detail=resp_dict.get("detail", "Unknown error"),
                )
            return resp_dict.get("detail", False)
