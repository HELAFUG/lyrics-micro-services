from fastapi import APIRouter
from core.schemas.author import AuthorCreate

router = APIRouter()


@router.post("/authors")
async def new_author(author: AuthorCreate):
    return author
