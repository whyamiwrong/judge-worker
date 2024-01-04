from fastapi import FastAPI
from fastapi import APIRouter
from datetime import datetime
from fastapi import HTTPException
import subprocess
from fastapi.responses import JSONResponse
router = APIRouter(prefix="/submit")



app = FastAPI()



@router.post("/create_cpp_file")
async def create_cpp_file(code_data: dict):
    try:
        if "code" not in code_data:
            raise HTTPException(status_code=422, detail="코드가 제공되지 않았습니다.")

        code = code_data["code"]
        filename = "muyaho.cpp"

        with open(filename, "w") as file:
            file.write(code)

        return {"message": f"C++ 파일 생성 성공: {filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"에러 발생: {str(e)}")


@router.post("/check_answer")
async def check_answer(code: dict):
    try:
        
        newcode = code["code"]
        input_txt = code["inputs"]
        check_output = code["checks"]
        
        for idx, input_txt in enumerate(input_txt):
            print("testt")
            with open("input.txt", "w") as file:
                file.write(input_txt)
        
            with open("muyaho.cpp","w") as file:
                file.write(newcode)
            
            
            result_compile = subprocess.run(["g++", "muyaho.cpp", "-o", "muya_output"], capture_output=True, text=True, cwd="/workspace/whywrong/judge-worker")
            
            if result_compile.returncode != 0:
                print("Compilation Error")
                return {"correct": 2}
            with open("input.txt", "r") as input_file:
                result_execution = subprocess.run(["./muya_output"], input=input_file.read(), stdout = subprocess.PIPE, text=True, cwd="/workspace/whywrong/judge-worker")
            print("test2")
            print(type(result_execution.stdout))
            print(result_execution.stdout)
            if result_execution.stdout.strip() != check_output[idx].strip():
                correct = 2
                print("땡")
                print(result_execution.stdout)
                print(check_output[idx].strip())
                return {"correct":2}
        
        
        
        print(1)
        '''print(type(result_execution.stdout))'''
        '''return {"result": result_execution}'''
        '''return {"result": result_execution.stdout, 
               "correct": correct}'''
        return {"correct":1}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing C++ code: {e.output}")
        
        
@router.get("/hello-world")
async def hello():
    return "hello, world!"


@router.get("/now")
async def now():
    return datetime.now()



app.include_router(router)