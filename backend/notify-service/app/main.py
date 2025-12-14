import uvicorn
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.config import settings
from api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=settings.log.level,
        format=settings.log.format,
        datefmt=settings.log.datefmt,
    )
    yield


app = FastAPI(
    title="Lyrics Notify Service",
    description="Lyrics API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.srv.host,
        port=settings.srv.port,
        reload=settings.srv.reload_on_change,
    )
