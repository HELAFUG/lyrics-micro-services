import logging
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from taskiq import TaskiqDepends
from core import broker
from core.models import User, db_helper
from repository.user import get_user_by_id
from service.http.notify_service import after_register

log = logging.getLogger(__name__)


@broker.task
async def welcome_email_notification(
    user_id: int,
    session: Annotated[AsyncSession, TaskiqDepends(db_helper.session_getter)],
):
    user: User = await get_user_by_id(session=session, user_id=user_id)
    await after_register(user_email=user.email)
    log.info("Sending welcome email to user %r", user_id)
