from fastapi import APIRouter
from datetime import datetime

from fastapi import FastAPI
from fastapi import HTTPException

from typing import Optional, Dict
import subprocess

router = APIRouter(prefix="/health")

@router.get("/hihi")
async def hihi():
    return {"result": "hello"}

@router.post("/execute_shell")
async def execute_shell(
    command_json: Optional[Dict[str, str]] = None,
):
    print(1)
    if not command_json:
        raise HTTPException(status_code=422, detail="Command cannot be empty")

    if command_json:
        # JSON 형식으로 데이터가 전달된 경우 처리
        command = command_json.get("command", "")

    try:
        result = subprocess.check_output(command, shell=True, text=True)
        print("Command executed: ", command)
        return {"result": result}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error executing shell command: {e}")
        

@router.get("/hello-world")
async def hello():
    
    return "hello, world!"

@router.get("/now")
async def now():
    return datetime.now()

app = FastAPI()

app.include_router(router)