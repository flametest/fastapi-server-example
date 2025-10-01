import fastapi

from app.api.v1.routes.auth.auth import router as auth_router
from app.api.v1.routes.user.user import router as user_router

router = fastapi.APIRouter()

router.include_router(prefix="/v1", router=user_router)
router.include_router(prefix="/v1", router=auth_router)
