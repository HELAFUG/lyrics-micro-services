from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AuthServiceConfig(BaseModel):
    url: str = "http://localhost:8040"

    @property
    def register_url(self):
        return f"{self.url}/api/v1/auth/register"

    @property
    def login_url(self):
        return f"{self.url}/api/v1/auth/login"


class Settings(BaseSettings):
    auth_service: AuthServiceConfig = AuthServiceConfig()


settings = Settings()
