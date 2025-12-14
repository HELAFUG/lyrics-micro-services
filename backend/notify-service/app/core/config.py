from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

load_dotenv()


class UserServiceConfig(BaseModel):
    url: str = getenv("USER_SERVICE_URL")

    @property
    def register_url(self):
        return self.url + "/api/v1/auth/register"

    @property
    def login_url(self):
        return self.url + "/api/v1/auth/login"


class LogConfig(BaseModel):
    level: str = "INFO"
    format: str = LOG_FORMAT
    datefmt: str = "%Y-%m-%d %H:%M:%S %z"


class SRVConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8050
    reload_on_change: bool = True


class AdminConfig(BaseModel):
    email: str = getenv("ADMIN_EMAIL")
    password: str = getenv("ADMIN_PASSWORD")


class APIConfig(BaseModel):
    prefix: str = "/api/"
    notify: str = "/notify-service/"


class Settings(BaseSettings):
    user_service: UserServiceConfig = UserServiceConfig()
    srv: SRVConfig = SRVConfig()
    api: APIConfig = APIConfig()
    log: LogConfig = LogConfig()
    admin: AdminConfig = AdminConfig()


settings = Settings()
