from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientConnectorError
from core.config import settings
from fastapi import HTTPException


async def fetch_exist_user(email: str) -> bool:
    async with ClientSession() as session:
        async with session.get(
            f"{settings.external.auth.check_user_exist}/{email}"
        ) as response:
            try:
                resp_dict = await response.json()
                if response.status != 200:
                    raise HTTPException(
                        status_code=response.status,
                        detail=resp_dict.get("detail", "Unknown error"),
                    )

            except ClientConnectorError as e:
                raise HTTPException(
                    status_code=400, detail=str("External service error")
                )
            return resp_dict.get("detail", False)
