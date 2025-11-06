from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.crud.user import create_user, get_user_by_email
from app.schemas.user import UserCreate


def register_user_service(db, data: UserCreate):
    """회원 등록 서비스 로직"""
    existing_user = get_user_by_email(db, data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="이미 가입된 이메일입니다."
        )
    user = create_user(db, data)
    return user
