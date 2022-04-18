import json
from datetime import datetime
import pandas as pd
import hashlib
from config import conn, VERTEX_RESSOURCE, VERTEX_TAG, EDGE_HAS_TAGS, VERTEX_NOTE, EDGE_HAS_TYPE, VERTEX_TYPE, \
    VERTEX_HIGHLIGHTS, EDGE_HAS_HIGHLIGHTS, VERTEX_DATE, EDGE_HAS_DATE, EDGE_HAS_SCORE_RESOURCE, EDGE_HAS_SCORE_NOTE, \
    VERTEX_USER, EDGE_HAS_RESOURCE
from graph_gen.helper_funcs import process_url
from model.resource import Resource
from services.tag_service import get_simlarity, get_score
from services.vertex_service import get_all_ressources_id

CSV_FILE_NAME = "resource_data.csv"


def prepareResource(res: Resource):
    res_id = hashlib.sha1(str(res.url).encode('utf-8')).hexdigest()
    domain_url = process_url(res.url)
    res.id = res_id
    res.domain = domain_url
    res.date = datetime.now()
    res.tags = [t.replace(", ", "").lower() for t in res.tags]
    res.user = "User_1"
    if "youtube" in res.domain:
        res.type = "Video"
    else:
        res.type = "Website"
    print(res.json())
    ##find_node()
    return res


## Add data to tigergraph. Add Data to Edges and Vertices
def add_data_to_vertex(res: Resource):
    res = prepareResource(res)
    add_user_to_resource(res)
    add_highlights_to_resource(res)
    add_date_to_resource(res)
    add_type_to_resource(res)
    add_resource(res)
    add_tag_to_ressource(res)
    add_resource_to_note(res)
    add_data_local_csv_file(res)
    add_domain_to_resource(res)


def add_highlights_to_resource(res: Resource):
    conn.upsertVertex(VERTEX_HIGHLIGHTS, res.id + "_highlights", attributes={"highlights_list": res.highlights})
    conn.upsertEdge(VERTEX_RESSOURCE, res.id, EDGE_HAS_HIGHLIGHTS, VERTEX_HIGHLIGHTS, res.id + "_highlights")


def add_date_to_resource(res: Resource):
    conn.upsertVertex(VERTEX_DATE, str(res.date))
    conn.upsertEdge(VERTEX_RESSOURCE, res.id, EDGE_HAS_DATE, VERTEX_DATE, str(res.date))


def add_domain_to_resource(res: Resource):
    conn.upsertVertex("domain", res.domain)
    conn.upsertEdge(VERTEX_RESSOURCE, res.id, "has_domain", "domain", res.domain)


def add_type_to_resource(res: Resource):
    conn.upsertEdge(VERTEX_RESSOURCE, res.id, EDGE_HAS_TYPE, VERTEX_TYPE, res.type)


def add_user_to_resource(res: Resource):
    conn.upsertVertex(VERTEX_USER, res.user, {"name": res.user})
    conn.upsertEdge(VERTEX_USER, res.user, EDGE_HAS_RESOURCE, VERTEX_RESSOURCE, res.id)


def add_resource(res: Resource):
    conn.upsertVertex(VERTEX_RESSOURCE, res.id, attributes={"url": res.url, "title": res.title})


## Add note to ressource and vectorize note
def add_resource_to_note(res: Resource):
    vector_score = get_score(res.notes)
    vector_score = vector_score.tolist()
    conn.upsertVertex(VERTEX_NOTE, res.id + "_note", attributes={"text": res.notes, "value": vector_score})


## Add every tag to specific resource
def add_tag_to_ressource(res: Resource):
    for tag in res.tags:
        conn.upsertVertex(VERTEX_TAG, tag, {"value": tag})
        conn.upsertEdge(VERTEX_RESSOURCE, res.id, EDGE_HAS_TAGS, VERTEX_TAG, tag)


def add_data_local_csv_file(res: Resource):
    data = json.loads(res.json())
    df = pd.json_normalize(data)
    df.to_csv(CSV_FILE_NAME, mode='a', index=False, encoding='utf-8', header=False)


def get_all_resource_ids_link_to_each_other(id, title):
    result_id = get_all_ressources_id()
    for key, value in result_id.items():
        score = get_simlarity(value['title'], title)
        conn.upsertEdge(VERTEX_RESSOURCE, value['id'], "score", VERTEX_RESSOURCE, id, {"value": score})
    return ""
