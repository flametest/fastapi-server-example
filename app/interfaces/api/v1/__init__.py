import fastapi
from .routes.user import router as user_router
from .routes.auth import router as auth_router

router = fastapi.APIRouter()

router.include_router(prefix="/v1", router=user_router)
router.include_router(prefix="/v1", router=auth_router)
