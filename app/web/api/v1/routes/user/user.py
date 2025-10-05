from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.enum import Gender
from app.core.exception import BadRequestError, NotFoundError
from app.infra.models.user import UserModel
from app.service.user_service import UserService, get_user_service
from app.web.api.v1.dependencies.auth import get_current_user, get_password_hash
from app.web.api.v1.dependencies.db import DB
from app.web.api.v1.routes.user.schema import UserCreate, UserDetail

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=dict)
async def register(
    user_create: UserCreate,
    db: DB,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    # check if the email exist
    user = await user_service.get_user_by_email(user_create.email)
    if user:
        raise BadRequestError(
            "Email already registered",
        )

    # check if the username exist
    user = await user_service.get_user_by_username(user_create.username)
    if user:
        raise NotFoundError(
            "Username already registered",
        )

    # create new user
    hashed_password = get_password_hash(user_create.password.get_secret_value())
    db_user = UserModel(
        email=user_create.email,
        username=user_create.username,
        password=hashed_password,
        gender=user_create.gender.value if user_create.gender else None,
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return {"message": "User registered successfully"}


@router.get("/me")
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@router.get(path="/{user_id}")
async def get_user_detail(
    user_id: int,
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> UserDetail:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise NotFoundError(
            "User not found",
        )
    return UserDetail(
        id=user.id,
        email=user.email,
        username=user.username,
        gender=Gender(user.gender),
    )
