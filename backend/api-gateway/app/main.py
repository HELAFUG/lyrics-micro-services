import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import api_gateway_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_gateway_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level=logging.INFO,
    )
