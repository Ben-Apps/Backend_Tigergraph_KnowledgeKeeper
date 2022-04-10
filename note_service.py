import json
import pandas as pd
import hashlib
from config import conn, VERTEX_RESSOURCE, VERTEX_TAG, EDGE_HAS_TAGS, VERTEX_NOTE, EDGE_HAS_TYPE, VERTEX_TYPE
from model.resource import Resource
from tag_service import get_top_rank_topics, get_score, get_simlarity
from vertex_service import get_all_ressources_id

CSV_FILE_NAME = "resource_data.csv"


## Add data to tigergraph. Add Data to Edges and Vertices
def add_data_to_vertex(res: Resource):
    # local save
    add_data_local_csv_file(res)
    # create hash
    id = hashlib.sha256(str(res.url).encode('utf-8')).hexdigest()

    conn.upsertVertex(VERTEX_RESSOURCE, id, attributes={"url": res.url, "title": res.title})
    get_all_resource_ids_link_to_each_other(id, res.title)
    conn.upsertEdge(VERTEX_RESSOURCE, id, EDGE_HAS_TYPE, VERTEX_TYPE, "Website")
    ##add_tag_to_ressource(res.tags, id)
    ##conn.upsertVertex(VERTEX_NOTE, id, attributes={"text": res.learningDiary})
    ##conn.upsertVertex("type", "Website", attributes={"text": res.learningDiary})
    # conn.upsertEdge("Entity_Name", ent.text, "ENTITY_NAME_ENTITY", "Entity", ent.label_)

    return ""


def get_all_resource_ids_link_to_each_other(id, title):
    result_id = get_all_ressources_id()
    for key, value in result_id.items():
        score = get_simlarity(value['title'], title)
        conn.upsertEdge(VERTEX_RESSOURCE, value['id'], "score", VERTEX_RESSOURCE, id, {"value": score})
    return ""


## Add every tag to specific resource
def add_tag_to_ressource(tags: list, ressourceId):
    for tag in tags:
        conn.upsertEdge(VERTEX_RESSOURCE, ressourceId, EDGE_HAS_TAGS, VERTEX_TAG, tag)


def add_data_local_csv_file(res: Resource):
    data = json.loads(res.json())
    df = pd.json_normalize(data)
    df.to_csv(CSV_FILE_NAME, index=False, encoding='utf-8')
