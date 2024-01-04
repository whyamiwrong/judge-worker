from fastapi import FastAPI

from routes.health import router as health
from routes.submit import router as submit
from starlette.middleware.cors import CORSMiddleware

origins=["http://localhost:3000",
        "http://localhost"]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health, tags=["헬스체크"])
app.include_router(submit, tags=["코드제출"])



