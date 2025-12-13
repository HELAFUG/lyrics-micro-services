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


class APIConfig(BaseModel):
    prefix: str = "/api"


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


class Settings(BaseSettings):
    log: LogConfig = LogConfig()
    api_v1: APIV1 = APIV1()
    api: APIConfig = APIConfig()
    srv: SRVConfig = SRVConfig()
    db: DBConfig = DBConfig()


settings = Settings()
