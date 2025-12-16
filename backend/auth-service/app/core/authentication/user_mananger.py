import logging
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from core.models.mixins import IdIntPkMixin
from core.config import settings
from core.models import User
from tasks import welcome_email_notification, login_email_notification

log = logging.getLogger(__name__)


class UserManager(IdIntPkMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Request | None = None):
        log.info("User signed up %s", user.id)
        await welcome_email_notification.kiq(user.id)

    async def on_after_login(self, user, request: Request, response=None):
        log.info("User logged in %s", user.id)
        await login_email_notification.kiq(user.id)
