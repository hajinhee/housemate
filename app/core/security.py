from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

# .env 파일 불러오기
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data):
    """
    로그인 성공 시 JWT 토큰을 생성하는 함수: payload(data)를 받아 JWT access token 생성
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token):
    """
    클라이언트가 보낸 토큰이 유효한지 확인하는 함수: JWT token 검증 후 payload 반환
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
