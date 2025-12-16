from aiohttp import ClientSession
from core.config import settings
from core.schemas.user import UserCreate


async def register_new_user(
    user: UserCreate,
):
    async with ClientSession() as session:
        async with session.post(
            settings.auth_service.register_url,
            json={
                "email": user.email,
                "password": user.password,
            },
        ) as response:
            if response.status == 400:
                return {
                    "status": response.status,
                    "json": await response.json(),
                }
            resp = await response.json()
            return {
                "status": response.status,
                "json": resp,
            }


async def login_exist_user(user: UserCreate):
    async with ClientSession() as session:
        async with session.post(
            settings.auth_service.login_url,
            data={
                "grant_type": "",  # Optionally set this if needed
                "username": user.email,
                "password": user.password,
                "scope": "",  # Optional, based on your requirements
                "client_id": "",  # Optional, based on your requirements
                "client_secret": "",  # Optional, based on your requirements
            },
            headers={
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
        ) as response:
            resp = await response.json()
            return {
                "status": response.status,
                "json": resp,
            }
