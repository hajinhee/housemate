from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies import get_current_user
from app.schemas.user import UserCreate, UserRead, UserResponse
from app.services.user_service import register_user_service

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def register_user(request: UserCreate, db: Session = Depends(get_db)):
    """회원 등록 API"""
    user = register_user_service(db, request)
    return user


# @router.get("/")
# def register(request: UserCreate, db=Depends(get_db)):
#     """회원 정보 조회"""
#     return register_user(db, request)


# @router.put("/me", response_model=UserRead)
# def get_me(current_user=Depends(get_current_user)):
#     """회원 정보 업데이트"""
#     return current_user


# @router.post("/me/deletion", response_model=UserRead)
# def get_me(current_user=Depends(get_current_user)):
#     """회원 탈퇴 요청"""
#     return current_user


# @router.delete("/me/deletion", response_model=UserRead)
# def get_me(current_user=Depends(get_current_user)):
#     """회원 탈퇴 철회"""
#     return current_user
