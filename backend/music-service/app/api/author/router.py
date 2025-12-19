from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas.author import AuthorCreate
from core.models import db_helper
from service.author import create_new_author

router = APIRouter()


@router.post("/new-author")
async def new_author(
    author: AuthorCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await create_new_author(session=session, author_in=author)
