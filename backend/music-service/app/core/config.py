from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class AuthServiceConfig(BaseSettings):
    auth_service_url: str = "http://localhost:8040"

    @property
    def check_user_exist(self):
        return f"{self.auth_service_url}/api/service-api/users/check_exist_user"


class ExternalServices(BaseModel):
    auth: AuthServiceConfig = AuthServiceConfig()


class APIV1(BaseModel):
    prefix: str = "/v1"
    authors: str = "/authors"
    tracks: str = "/tracks"


class APIConfig(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()


class SRVSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8060
    reload_on_change: bool = True


class DBConfig(BaseModel):
    url: str = getenv("DB_URL")
    echo: bool = False


class Settings(BaseModel):
    api: APIConfig = APIConfig()
    srv: SRVSettings = SRVSettings()
    external: ExternalServices = ExternalServices()
    db: DBConfig = DBConfig()


settings = Settings()
