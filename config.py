import pyTigerGraph as tg

HOST = 'https://56c5cec09bbe4198b521e59b0a080ac8.i.tgcloud.io/'
USERNAME = 'tigergraph'
PASSWORD = 'test123'
GRAPHNAME = 'ressource_graph'

conn = tg.TigerGraphConnection(host=HOST, username=USERNAME, password=PASSWORD,
                               graphname=GRAPHNAME)
conn.apiToken = conn.getToken(conn.createSecret())


VERTEX_RESSOURCE = "ressource"
VERTEX_HIGHLIGHTS = "highlights"
VERTEX_TAG = "Tag"
VERTEX_NOTE = "note"
VERTEX_TYPE = "Type"
VERTEX_DATE = "date"
VERTEX_USER = "user"

EDGE_HAS_TAGS = "has_tags"
EDGE_HAS_TYPE = "has_type"
EDGE_HAS_HIGHLIGHTS = "has_highlights"
EDGE_HAS_DATE = "has_date"
EDGE_HAS_SCORE_RESOURCE = "score"
EDGE_HAS_SCORE_NOTE = "score_note"
EDGE_HAS_RESOURCE= "has_resource"


