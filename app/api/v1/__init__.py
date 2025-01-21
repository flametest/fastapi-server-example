import fastapi
from .routes.user import router as user_router

router = fastapi.APIRouter()

router.include_router(prefix="/v1", router=user_router)
