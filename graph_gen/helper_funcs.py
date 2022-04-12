from datetime import datetime
from hashlib import new
import tldextract
import time 

def get_value(dict_list,key_):
    values = [ sub[key_] for sub in dict_list ]
    return values

def common_tag_nodes(new_node_tag,input_nodes):
    # returns list of nodes with common tag
    common_tag_nodes_list=[]
    for node in input_nodes:
        if node['Tag']==new_node_tag:
            common_tag_nodes_list.append(node)
    return common_tag_nodes_list


def process_url_list(url):
    domain_list=[]
    for node_url in url:
        domain_list.append(process_url(node_url))
    return domain_list

def process_url(url):
    return tldextract.extract(url).domain

def check_domain(new_node_url,domain_list):
    url_feature=[]
    for domain in domain_list:
        if domain==new_node_url:
            url_feature.append(1)
        else:
            url_feature.append(0)
    return url_feature

def jaccard_similarity(x,y):
  # returns the jaccard similarity between two lists
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  return intersection_cardinality/float(union_cardinality)

def process_notes(new_node_notes, note_list):
    notes_feature=[]
    for note in note_list:
        notes_feature.append(jaccard_similarity(new_node_notes,note))
    return notes_feature

def process_dates(new_node_date, date_list):
    date_diff=[]
    new_date=datetime.strptime(new_node_date, '%Y-%m-%d')
    for date_string in date_list:
        datetime_ = datetime.strptime(date_string, '%Y-%m-%d')
        time_passed= new_date - datetime_
        # time_int=int(time.mktime((time_passed).timetuple()))
        date_diff.append(time_passed.seconds)
    # normalise
    minimum_time_passed = min(date_diff)
    normalized_diff = [i - minimum_time_passed for i in date_diff]
    return normalized_diff

def rank(url_feature,notes_feature,date_feature):
    similarity_features=[]
    for f in range(len(url_feature)):
        weighted_avergae = url_feature[f]/3 + notes_feature[f]/3 + date_feature[f]/3
        similarity_features.append(weighted_avergae)
    
    # Find the index with maximum similarity
    max_index=similarity_features.index(max(similarity_features))
    return max_index
