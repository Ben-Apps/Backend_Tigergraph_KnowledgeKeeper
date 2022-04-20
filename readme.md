
# Introduction

This is our backend that process the data from the browser extension. It is connected with our tigergraph instance. For the
data processing we use basic string operations and spacy for nlp tasks.
Moreover it is able to execute some queries from tigergraph that can be send to a frontend to use it in graph framework like: https://g6.antv.vision/zh

### Install Instructions:

1. Install all requirements:
   pip install -r requirements.txt
2. Install spacy:
   python -m spacy download en_core_web_sm
3. Change config.py data to your tigergraph instance

### Start Application/Backend

uvicorn main:app --reload

## Endpoints:

### post information from browser extension (notes, highlights, url, website)
@app.post("/notes")

### get all resources by specific tag
GET ("/tag/{tag}")

### get related concepts of a specific word
GET ("/domain/{word}")

### post website text and get sugesstions of tags
POST ("/tags")

### get information about a specific resource
GET ("/resource/{id}")

## Project

/scripts: Here find a script to extract the domain knowledge dataset to a file
that can be used for tigergraph mapping. It splits every relation in one
csv file.

/images: Screenshots of example graphs in tigergraph

/services/note_service: Push data to tigergraph

/services/vertex_service: Get data from tigergraph and put it in a good json way.

/data: here you can find a example csv of collected data by browser extension


### Dataset

Computer Science Ontology:

https://cso.kmi.open.ac.uk/downloads

### Links
https://fastapi.tiangolo.com/
https://spacy.io/

