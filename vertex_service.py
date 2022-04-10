from config import conn


## get all ids of resources
def get_all_ressources_id():
    gQuery = conn.runInstalledQuery("get_ressource_by_user")[0]["results"]
    result = {}
    count = 0
    print(gQuery)
    for p in gQuery:
        print(p['v_id'])
        result[count] = {
            "id": p['v_id'],
            "title": p['attributes']['title']
        }
        count += 1
    print(result)
    return result
