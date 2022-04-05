from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI
import pyTigerGraph as tg
from fastapi.middleware.cors import CORSMiddleware
import config as Credential

conn = tg.TigerGraphConnection(host=Credential.HOST, username=Credential.USERNAME, password=Credential.PASSWORD,
                               graphname=Credential.GRAPHNAME)
conn.apiToken = conn.getToken(conn.createSecret())

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Resource(BaseModel):
    id: str
    url: str
    notes: str


@app.get("/resource")
async def resource():
    gQuery = conn.runInstalledQuery("get_ressource_by_user")[0]
    count = 0
    return {"message": f"{gQuery}"}


@app.post("/notes")
async def resource(resource: Resource):
    print(resource)
