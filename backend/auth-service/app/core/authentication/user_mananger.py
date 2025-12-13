import logging
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from core.config import settings
from core.models import User

log = logging.getLogger(__name__)


class UserManager(UUIDIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Request | None = None):
        log.info("User signed up %s", user.id)
