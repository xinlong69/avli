from fastapi import APIRouter

from apps.agent.app.api.routes import utils

from apps.agent.app.api.routes import items

# from app.core.config import settings

api_router = APIRouter()
api_router.include_router(utils.router)
api_router.include_router(items.router)


# if settings.ENVIRONMENT == "local":
#     api_router.include_router(some_private_router.router)
