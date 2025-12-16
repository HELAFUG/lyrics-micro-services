from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas.author import AuthorCreate
from core.models import Author


async def create_author(
    author_in: AuthorCreate, session: AsyncSession
) -> Author | None:
    new_author = Author(**author_in.model_dump())
    session.add(new_author)
    await session.commit()
    return new_author
