from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import settings


class DBHelper:
    def __init__(self, db_url: str, echo: bool):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

    async def dispose(self):
        await self.engine.dispose()


db_helper = DBHelper(
    db_url=settings.db.url,
    echo=settings.db.echo,
)
