import logging
from core.config import settings
from aiohttp import ClientSession

log = logging.getLogger(__name__)


async def after_register(user_email: str):
    async with ClientSession(base_url=settings.notify_service.url) as session:
        async with session.post(
            f"{settings.notify_service.after_register_url}/{user_email}"
        ) as response:
            match response.status:
                case 200:
                    log.info("Email sent to %s", user_email)
                case 422:
                    log.error("Email is not correct %s", user_email)

                case _:
                    log.error("Error sending email to %s", user_email)


async def after_login(user_email: str):
    async with ClientSession(base_url=settings.notify_service.url) as session:
        async with session.post(
            f"{settings.notify_service.after_login_url}/{user_email}"
        ) as response:
            match response.status:
                case 200:
                    log.info("Email sent to %s", user_email)
                case 422:
                    log.error("Email is not correct %s", user_email)

                case _:
                    log.error("Error sending email to %s", user_email)
