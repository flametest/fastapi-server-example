from pydantic import BaseModel, EmailStr

from app.core.enum import Gender


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    gender: Gender | None = None


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr
    gender: Gender
