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


class Settings(BaseSettings):
    log: LogConfig = LogConfig()
    api_v1: APIV1 = APIV1()
    api: APIConfig = APIConfig()
    srv: SRVConfig = SRVConfig()
    db: DBConfig = DBConfig()


settings = Settings()
