from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from service.auth_external import fetch_exist_user
from core.schemas.author import AuthorCreate
from repository.author import create_author


async def create_new_author(session: AsyncSession, author_in: AuthorCreate):
    user_exist = await fetch_exist_user(email=author_in.email)
    if user_exist == False:
        raise HTTPException(status_code=400, detail="User not exist")

    author = await create_author(author_in=author_in, session=session)
    return author
