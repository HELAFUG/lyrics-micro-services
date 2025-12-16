from fastapi import APIRouter
from api.auth import auth_router

api_gateway_router = APIRouter(prefix="/api-gateway")
api_gateway_router.include_router(router=auth_router)
