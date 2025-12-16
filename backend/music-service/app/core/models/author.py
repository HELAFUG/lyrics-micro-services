from sqlalchemy.orm import Mapped, mapped_column
from core.models import Base


class Author(Base):
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    listens: Mapped[str] = mapped_column(nullable=True)
    genre: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    region: Mapped[str] = mapped_column(nullable=True)
