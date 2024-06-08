import time
import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


app = FastAPI()
allow_all = ['*']
app.add_middleware(
   CORSMiddleware,
   allow_origins=allow_all,
   allow_credentials=True,
   allow_methods=allow_all,
   allow_headers=allow_all
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["Owner-Code"] = "BY-RF-101"
    return response

@app.get("/")
async def root():
    return {"message": "I am alive!!!"}

@app.post("/sum")
async def sum(request: Request):
    try:
        req = await request.json()
        n1 = req['number1']
        n2 = req['number2']
        total = n1 + n2
        return JSONResponse(content={'message': 'Operation successfully complated.', 'Total': total}, status_code=200)    
    except BaseException as e:
        return HTTPException(detail={'message': 'Error in operation.'}, status_code=400)
    
@app.post("/user/role")
async def get_user_role(request: Request):
    if(request['id'] in ["Huginn", "Muninn"]):
        return JSONResponse(content={'message': 'Operation successfully complated.', 'role': 'User'}, status_code=200)
    elif(request['id'] in ["Odin", "Loki"]):
        return JSONResponse(content={'message': 'Operation successfully complated.', 'role': 'Admin'}, status_code=200)
    else:
        return HTTPException(detail={'message': 'User not found.'}, status_code=404)
