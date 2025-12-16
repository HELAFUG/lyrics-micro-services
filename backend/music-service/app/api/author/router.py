from fastapi import APIRouter
from core.schemas.author import AuthorCreate
from service.auth_external import fetch_exist_user

router = APIRouter()


@router.post("/new-author")
async def new_author(author: AuthorCreate):
    pass
