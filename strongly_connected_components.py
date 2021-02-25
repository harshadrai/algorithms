def find_connected_components(graph,start_node,nodes_seen,connected_components=None):
    if not connected_components:
        connected_components=[]
    nodes_seen.append(start_node)
    for neighbor_node in graph[start_node]['outgoing']:
        if neighbor_node not in nodes_seen:
            connected_components,nodes_seen=find_connected_components(graph,neighbor_node,nodes_seen,connected_components)
    connected_components.append(start_node)
    return connected_components,nodes_seen


def ranking_of_reversed_graph(graph,start_node,node_rank,node_ranking,nodes_seen):
    nodes_seen.append(start_node)
    for neighbor_node in graph[start_node]['incoming']:
        if neighbor_node not in nodes_seen:
            node_rank,node_ranking,nodes_seen=ranking_of_reversed_graph(graph,neighbor_node,node_rank,node_ranking,nodes_seen)
    node_rank+=1
    node_ranking[node_rank]=start_node
    return node_rank,node_ranking,nodes_seen

def strongly_connected_components(graph):
    node_rank=0
    nodes_seen=[]
    node_ranking={}
    for node in graph.keys():
        if node not in nodes_seen:
            node_rank,node_ranking,nodes_seen=ranking_of_reversed_graph(graph,node,node_rank,node_ranking,nodes_seen)
    nodes_seen=[]
    strongly_connected_components=[]
    for i in range(node_rank,0,-1):
        if node_ranking[i] not in nodes_seen:
            connected_components,nodes_seen=find_connected_components(graph,node_ranking[i],nodes_seen)
            strongly_connected_components.append(connected_components)
    return strongly_connected_components


graph = {'A': {'outgoing':['B'],'incoming':['C']},
         'B': {'outgoing':['C'],'incoming':['A']},
         'C': {'outgoing':['D','A'],'incoming':['B']},
         'D': {'outgoing':['E'],'incoming':['F']},
         'E': {'outgoing':['F'],'incoming':['D']},
         'F': {'outgoing':['D'],'incoming':['E']}
         }

strongly_connected_components(graph)
