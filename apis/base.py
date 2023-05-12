from fastapi import APIRouter
from apis.version_1 import router_important, router_category, router_task

api_router = APIRouter(prefix="/v1")

api_router.include_router(router_important.router, prefix="/important", tags=["important"])
api_router.include_router(router_category.router, prefix="/categories", tags=["categories"])
api_router.include_router(router_task.router, prefix="/tasks", tags=["tasks"])