from typing import Optional

from pydantic import BaseModel, EmailStr
from app.schemas.enum import Gender


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    gender: Optional[Gender]


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr
    gender: Gender
