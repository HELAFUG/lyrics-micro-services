import logging
from mailing.welcome.send_mail import send_email

log = logging.getLogger(__name__)


async def send_welcome_email(email: str) -> None:
    log.info("Sending welcome email to %s", email)
    await send_email(email, "Welcome to Lyrics", "Thanks for registering")
