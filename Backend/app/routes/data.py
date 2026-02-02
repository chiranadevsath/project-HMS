from fastapi import APIRouter

from app.routes import add, get

router = APIRouter(prefix="/data", tags=["data"])

router.include_router(add.router, tags=["add"])
router.include_router(get.router, tags=["get"])

