from config import conn


## get all ids of resources
def get_all_ressources_id():
    gQuery = conn.runInstalledQuery("get_ressource_by_user")[0]["results"]
    result = {}
    count = 0
    for p in gQuery:
        print(p['v_id'])
        result[count] = {
            "id": p['v_id'],
            "title": p['attributes']['title']
        }
        count += 1
    return result


def get_relations_of_specific_word(word: str):
    gQuery = conn.runInstalledQuery("get_super_topics_of_specific_word", {"word_query": word})[0]["@@list_concept"]
    ## remove empty strings
    filtered_list = list(filter(None, gQuery))
    children = []
    for w in filtered_list:
        children.append({
            "children": [],
            "collapsed": True,
            "id": w,
            "name": w,
        })
    return  {
        "name": "Resource Graph",
        "id": word,
        "children": children,
    }


def get_all_resources_by_tag(tag: str):
    gQuery = conn.runInstalledQuery("get_resource_by_tag", {"tag": tag})[0]["result"]
    children = []
    for v in gQuery:
        url = v["attributes"]["url"]
        title = v["attributes"]["title"]
        children.append({
            "children": [],
            "collapsed": True,
            "id": title,
            "name": url,
            "url": url
        })
    result = {
        "name": "Resource Graph",
        "id": tag,
        "children": children,
    }
    return result
