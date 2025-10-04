from pydantic import BaseModel, EmailStr, SecretStr

from app.core.enum import Gender


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: SecretStr
    gender: Gender | None = None


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr
    gender: Gender
