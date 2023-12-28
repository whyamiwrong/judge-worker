from fastapi import APIRouter

router = APIRouter(prefix="/algo")

@router.post("/submit")
async def submit():
    ""