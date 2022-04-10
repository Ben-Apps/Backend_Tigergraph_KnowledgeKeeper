from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from config import conn
from model.resource import Resource
from model.website import Website
from note_service import add_data_local_csv_file, add_data_to_vertex
from tag_service import get_top_rank_topics

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

## Endpoint to save data from browser extension
@app.post("/notes")
async def resource(resource: Resource):
    add_data_to_vertex(resource)
