from pydantic import BaseModel, EmailStr, SecretStr

from app.core.enum import Gender
from app.infra.models import UserModel


class User(BaseModel):
    id: int
    email: EmailStr
    username: str
    password: SecretStr
    gender: Gender | None

    @classmethod
    def from_db(cls, db_user: UserModel) -> "User":
        return cls(
            id=db_user.id,
            username=db_user.username,
            password=SecretStr(db_user.password),
            email=db_user.email,
            gender=Gender(db_user.gender),
        )
