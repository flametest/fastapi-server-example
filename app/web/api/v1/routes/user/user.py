from fastapi import APIRouter, Depends

from app.core.enum import Gender
from app.core.exception import BadRequestError, NotFoundError
from app.infra.models.user import User
from app.web.api.v1.dependencies.auth import get_current_user, get_password_hash
from app.web.api.v1.dependencies.db import DB
from app.web.api.v1.routes.user.schema import UserCreate, UserDetail

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=dict)
async def register(user: UserCreate, db: DB):
    # check if the email exist
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise BadRequestError(
            "Email already registered",
        )

    # check if the username exist
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise NotFoundError(
            "Username already registered",
        )

    # create new user
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        password=hashed_password,
        gender=user.gender.value if user.gender else None,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User registered successfully"}


@router.get("/me")
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@router.get(path="/{user_id}")
def get_user_detail(
    user_id: int,
    db: DB,
) -> UserDetail:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise NotFoundError(
            "User not found",
        )
    return UserDetail(
        id=db_user.id,
        email=db_user.email,
        username=db_user.username,
        gender=Gender(db_user.gender),
    )
