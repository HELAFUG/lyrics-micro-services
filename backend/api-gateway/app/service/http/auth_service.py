from aiohttp import ClientSession
from core.config import settings
from core.schemas.user import UserCreate


async def register_new_user(
    user: UserCreate,
):
    async with ClientSession() as session:
        try:

            async with session.post(
                settings.auth_service.register_url,
                json={
                    "email": user.email,
                    "password": user.password,
                },
            ) as response:

                return await response.json()

        except Exception as e:
            print(e)
