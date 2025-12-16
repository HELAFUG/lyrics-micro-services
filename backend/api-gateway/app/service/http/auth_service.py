from aiohttp import ClientSession, ClientResponse
from core.config import settings


async def register_new_user(email: str, password: str) -> ClientResponse:
    async with ClientSession() as session:
        async with session.post(
            settings.auth_service.register_url,
            data={"email": email, "password": password},
        ) as response:
            return await response
