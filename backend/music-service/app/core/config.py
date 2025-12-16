from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AuthServiceConfig(BaseSettings):
    auth_service_url: str = "http://localhost:8040"

    @property
    def check_user_exist(self):
        return f"{self.auth_service_url}/service-api/users/check_user_exist"


class ExternalServices(BaseModel):
    auth: AuthServiceConfig = AuthServiceConfig()


class APIV1(BaseModel):
    prefix: str = "/v1"
    profiles: str = "/profiles"
    tracks: str = "/tracks"


class APIConfig(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()


class SRVSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8060
    reload_on_change: bool = True


class Settings(BaseModel):
    api: APIConfig = APIConfig()
    srv: SRVSettings = SRVSettings()
    external: ExternalServices = ExternalServices()


settings = Settings()
