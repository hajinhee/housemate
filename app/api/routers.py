# app/api/routers.py
from fastapi import APIRouter
from app.api.endpoints import performance, user

api_router = APIRouter()

# 각각의 endpoint 라우터를 등록
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(
    performance.router, prefix="/performance", tags=["Performances"]
)
