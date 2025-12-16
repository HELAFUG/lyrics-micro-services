from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AuthServiceConfig(BaseSettings):
    auth_service_url: str = "http://localhost:8040"

    @property
    def check_user_exist(self):
        return f"{self.auth_service_url}/service-api/users/check_user_exist"
