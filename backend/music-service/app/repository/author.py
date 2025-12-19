from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.schemas.author import AuthorCreate
from core.models import Author


async def get_author(session: AsyncSession, email: str) -> Author | None:
    stmt = select(Author).where(Author.email == email)
    return (await session.execute(stmt)).scalars().first()


async def create_author(
    author_in: AuthorCreate, session: AsyncSession
) -> Author | None:
    exist_author = await get_author(session=session, email=author_in.email)
    if exist_author:
        return exist_author.email

    new_author = Author(**author_in.model_dump())
    session.add(new_author)
    await session.commit()
    return new_author
