import logging
from mailing.welcome.send_mail import send_email

log = logging.getLogger(__name__)


async def send_login_email(email: str) -> None:
    await send_email(
        email,
        "We are detecting some activity on your account",
        "Some you login into your account recently",
    )
    log.info("Sending login email to %s", email)
