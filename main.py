from fastapi import FastAPI

from routes.health import router as health
from routes.submit import router as submit

app = FastAPI()

app.include_router(health, tags=["헬스체크"])
app.include_router(submit, tags=["코드제출"])



