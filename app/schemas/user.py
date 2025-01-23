from pydantic import BaseModel, EmailStr

from app.schemas.enum import Gender


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr
    gender: Gender
