from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.resource import Resource
from model.website import Website
from services.note_service import add_data_to_vertex
from services.tag_service import get_top_rank_topics
from services.vertex_service import get_all_resources_by_tag, get_relations_of_specific_word

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
    return resource


# get all resources by specific tag
@app.get("/tag/{tag}")
async def resource(tag: str):
    query = get_all_resources_by_tag(tag)
    return query


# get related concept of specific word
@app.get("/domain/{word}")
async def get_relations(word: str):
    return get_relations_of_specific_word(word)


## get suggestions for tag
@app.post("/tags")
async def resource(website: Website):
    return get_top_rank_topics(website.url)


## get information about a specific resource
@app.get("/resource/{id}")
async def get_resource_tag():
    return ""
