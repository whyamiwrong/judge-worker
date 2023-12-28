from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/health")


@router.get("/hello-world")
async def hello():
    return "hello, world!"


@router.get("/now")
async def now():
    return datetime.now()
