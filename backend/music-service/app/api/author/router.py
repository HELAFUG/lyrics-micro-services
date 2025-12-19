from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
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
    result = await create_new_author(session=session, author_in=author)
    if result:
        return result
    raise HTTPException(
        status_code=400, detail=f"User with email {author.email} already exist"
    )
