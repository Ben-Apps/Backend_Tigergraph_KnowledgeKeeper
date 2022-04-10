import pyTigerGraph as tg

HOST = 'https://56c5cec09bbe4198b521e59b0a080ac8.i.tgcloud.io/'
USERNAME = 'tigergraph'
PASSWORD = 'test123'
GRAPHNAME = 'ressource_graph'

VERTEX_RESSOURCE = "ressource"
VERTEX_TAG = "Tag"
VERTEX_NOTE = "note"
VERTEX_TYPE = "Type"

EDGE_HAS_TAGS = "hasTags"
EDGE_HAS_TYPE = "has_type"


conn = tg.TigerGraphConnection(host=HOST, username=USERNAME, password=PASSWORD,
                               graphname=GRAPHNAME)
conn.apiToken = conn.getToken(conn.createSecret())
