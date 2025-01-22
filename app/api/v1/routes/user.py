import fastapi
from app.schemas.user import UserDetail

router = fastapi.APIRouter(prefix="/users", tags=["Users"])


@router.get(path="/{user_id}", response_model=UserDetail)
def get_user_detail(user_id: int):
    return UserDetail(id=user_id, username="", email="xx@gg.com")
