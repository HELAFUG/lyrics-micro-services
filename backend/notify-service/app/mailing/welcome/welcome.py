from mailing.welcome.send_mail import send_email


async def send_welcome_email(email: str) -> None:
    await send_email(email, "Welcome to Lyrics", "Thanks for registering")
