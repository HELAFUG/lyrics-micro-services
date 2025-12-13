import uuid

from fastapi_users import FastAPIUsers

from core.models import User
from api.dependencies.authentication import get_user_manager
from api.dependencies.authentication import authentication_backend

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)
