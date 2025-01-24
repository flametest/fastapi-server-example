from fastapi import APIRouter, Depends, HTTPException

from app.schemas.enum import Gender
from app.schemas.user import UserDetail, UserCreate
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.api.v1.dependencies.auth import get_current_user, get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=dict)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # 检查邮箱是否已存在
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 检查用户名是否已存在
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

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
def get_user_detail(user_id: int) -> UserDetail:
    return UserDetail(id=user_id, username="", email="xx@gg.com", gender=Gender.MALE)
