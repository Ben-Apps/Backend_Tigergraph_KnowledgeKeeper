import helper_funcs

def find_node(new_node,input_nodes):
    '''
    new_node : dictionary with the following keys - URL, Notes, Date, Tag, ID
    input_nodes - List of nodes with every element as a dictionary. The following keys should be present in every element:
    1) URL : string
    2) Notes : string
    4) Date : string
    5) Tag : string
    6) ID : ID of the node
    return: one of the input_nodes from the dictionary
    '''
    # Check if input nodes is empty (User is just starting up to form their graph)
    if len(input_nodes)==0:
        # call the GSQL to add just one node
        # Make sure returning id here doesnt make a self loop
        return new_node

    # Hard filter by Tag if tag already exists
    # Find common nodes to the particular input tag
    common_tag_nodes_list=helper_funcs.common_tag_nodes(new_node['Tag'],input_nodes)
    # if only one node with common tag attach to that node
    if len(common_tag_nodes_list)==1:
        return common_tag_nodes_list[0]

    # Process further nodes

    # Check if same URL domains exist 
    domain_list=helper_funcs.process_url_list(helper_funcs.get_value(common_tag_nodes_list,'URL'))
    url_feature=helper_funcs.check_domain(new_node['URL'],domain_list)

    # Similarity score from notes and highlights
    notes_feature=helper_funcs.process_notes(new_node['Notes'],helper_funcs.get_value(common_tag_nodes_list,'Notes'))
    
    # Get date features
    date_feature=helper_funcs.process_dates(new_node['Date'],helper_funcs.get_value(common_tag_nodes_list,'Date'))

    # Ranking of nodes and find the top most node
    max_index=helper_funcs.rank(url_feature,notes_feature,date_feature)

    return common_tag_nodes_list[max_index]



if __name__ == "__main__":
    node_dict=[{'URL':'http://forums.news.cnn.com/','Tag':'ML','Date':'2021-04-04','Notes':'I am doing machine learning','ID':'1'},
                {'URL':'http://forums.news.cnn.com/','Tag':'ML','Date':'2021-04-04','Notes':'I am doing machine learning','ID':'1'},
                {'URL':'http://forums.news.cnn.com/','Tag':'ML','Date':'2021-04-04','Notes':'I am doing machine learning','ID':'1'}]
    new_node={}
    find_node({'URL':'http://forums.news.cnn.com/','Tag':'ML','Date':'2021-04-04','Notes':'I am doing machine learning','ID':'1'},node_dict)