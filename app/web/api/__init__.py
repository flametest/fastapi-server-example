import fastapi

from .v1 import router as api_v1_router

router = fastapi.APIRouter()

router.include_router(router=api_v1_router)
