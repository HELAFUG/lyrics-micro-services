from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyUserDatabase,
    SQLAlchemyBaseUserTable as SQLAlchemyBaseUserTableGeneric,
)
from core.models import Base
from core.models.mixins import IdIntPkMixin


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .access_token import AccessToken


class SQLAlchemyBaseUserTable(SQLAlchemyBaseUserTableGeneric[int]):
    pass


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable):
    access_tokens: Mapped[list["AccessToken"]] = relationship(back_populates="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
