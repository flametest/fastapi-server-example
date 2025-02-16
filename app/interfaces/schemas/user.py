from typing import Optional, List

from pydantic import BaseModel, EmailStr, field_validator
from app.interfaces.schemas.enum import Gender


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    age: int
    gender: Optional[Gender]

    @classmethod
    @field_validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError('年龄必须在 0-150 之间')
        return v

    @classmethod
    @field_validator('gender')
    def validate_gender(cls, v):
        if v not in [Gender.MALE, Gender.FEMALE]:
            raise ValueError('性别必须是 male、female')
        return v


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr
    gender: Gender

    class Config:
        # deprecated
        orm_mode = True
        from_attributes = True


class UserListResponse(BaseModel):
    total: int
    items: List[UserDetail]
    page: int
    page_size: int
