from pydantic import BaseModel, EmailStr


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr
