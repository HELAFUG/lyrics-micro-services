from os import getenv
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

DEBUG = False
BASE_DIR = Path(__file__).parent.parent
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


class LogConfig(BaseModel):
    level: str = "INFO"
    format: str = LOG_FORMAT
    datefmt: str = "%Y-%m-%d %H:%M:%S"


class APIV1(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"


class APIConfig(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()

    @property
    def bearer_token_to_url(self):
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


class SRVConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8040
    reload_on_changes: bool = True


class DBConfig(BaseModel):
    url: str = getenv("DB_URL")
    echo: bool = True if DEBUG else False
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str = getenv("RESET_PASSWORD_TOKEN_SECRET")
    verification_token_secret: str = getenv("VERIFICATION_TOKEN_SECRET")


class NofifyService(BaseModel):
    url: str = getenv("NOTIFY_SERVICE_URL")

    @property
    def after_register_url(self):
        return self.url + "api/notify-service/after_register/"

    @property
    def after_login_url(self):
        return self.url + "api/notify-service/after-login/"


class TaskIQConfig(BaseModel):
    url: str = getenv("TASKIQ_URL", "amqp://guest:guest@localhost:5672/")


class Settings(BaseSettings):
    log: LogConfig = LogConfig()
    api_v1: APIV1 = APIV1()
    api: APIConfig = APIConfig()
    srv: SRVConfig = SRVConfig()
    db: DBConfig = DBConfig()
    access_token: AccessToken = AccessToken()
    notify_service: NofifyService = NofifyService()
    taskiq: TaskIQConfig = TaskIQConfig()


settings = Settings()

if DEBUG:
    settings.log.level = "DEBUG"
