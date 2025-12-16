from typing import Optional
from pydantic import BaseModel, EmailStr


class AuthorBase(BaseModel):
    username: str


class AuthorCreate(AuthorBase):
    email: EmailStr
    listens: Optional[str | None] = None
    genre: Optional[str | None] = None
    name: Optional[str | None] = None
    last_name: Optional[str | None] = None
    region: Optional[str | None] = None


class Author(AuthorBase):
    id: int
