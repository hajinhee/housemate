from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    uid: str


class UserLogin(BaseModel):
    email: str
    name: str


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
