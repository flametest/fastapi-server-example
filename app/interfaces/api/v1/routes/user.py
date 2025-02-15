from fastapi import APIRouter, Depends, HTTPException

from app.interfaces.schemas.user import UserDetail, UserCreate, UserListResponse
from app.interfaces.api.v1.dependencies.db import DB
from app.infrastructure.persistence.models.user import User
from starlette import status
from app.application.queries.query_factory import Que
from app.interfaces.api.v1.dependencies.auth import get_current_user, get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=dict)
async def register(user: UserCreate, db: DB):
    # 检查邮箱是否已存在
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # 检查用户名是否已存在
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    # 创建新用户
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        password=hashed_password,
        gender=user.gender.value
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User registered successfully"}


@router.get("/me")
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@router.get(path="/{user_id}", response_model=UserDetail)
def get_user_detail(user_id: int, db: DB, current_user=Depends(get_current_user)) -> UserDetail:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserDetail(id=db_user.id, email=db_user.email, username=db_user.username, gender=db_user.gender)


@router.get("/{user_id}/v1", response_model=UserDetail)
async def get_user(
        user_id: int,
        user_queries: UserQueries = Depends(Provider[UserQueries])
):
    return await user_queries.get_user_by_id(user_id)


@router.get("", response_model=UserListResponse)
async def list_users(
        skip: int = 0,
        limit: int = 10,
        query_factory: QueryFactory = Depends()
):
    user_queries = query_factory.create_user_queries()
    users = await user_queries.get_users(skip=skip, limit=limit)
    total = len(users)  # 实际项目中应该从数据库获取总数
    return UserListResponse(
        total=total,
        items=users,
        page=skip // limit + 1,
        page_size=limit
    )
