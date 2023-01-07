from fastapi import FastAPI
from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.openapi.utils import get_openapi
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from fastapi.responses import StreamingResponse
import subprocess 
# import json
from app import app 

app = FastAPI()
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/speed/", tags=["speed"])
def speed():
    my_iperf_process = subprocess.check_output(["iperf3","-c","speedtest.shinternet.ch", "-p 5200-5209","--forceflush", "-J"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    iperf_output = my_iperf_process.stdout.decode('utf-8')
    return iperf_output


if __name__ == "__main__":
    import uvicorn

    # for running locally
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8080,
    )
