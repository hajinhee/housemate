from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str):
    """이메일 조회 쿼리"""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, data: UserCreate):
    """회원 등록 쿼리"""
    user = User(email=data.email, name=data.name, uid=data.uid)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
