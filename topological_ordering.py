def depth_first_search(graph,start_node,topological_order_number,topological_ordering,nodes_seen):
    nodes_seen.append(start_node) 
    for neighbor_node in graph[start_node]['outgoing']:
        if neighbor_node not in nodes_seen:
            topological_order_number,topological_ordering,nodes_seen=depth_first_search(graph,neighbor_node,topological_order_number,topological_ordering,nodes_seen)
    topological_ordering[start_node]=topological_order_number
    topological_order_number-=1
    return topological_order_number,topological_ordering,nodes_seen

def topological_ordering(graph):
    topological_ordering={}
    topological_order_number=len(list(graph.keys()))
    nodes_seen=[]
    for node in list(graph.keys()):
        if node not in nodes_seen:
            topological_order_number,topological_ordering,nodes_seen=depth_first_search(graph,node,topological_order_number,topological_ordering,nodes_seen)
    return topological_ordering

graph = {'A': {'outgoing':['B', 'C'],'incoming':[]},
         'B': {'outgoing':['C', 'D'],'incoming':[]},
         'C': {'outgoing':['D','E'],'incoming':['B']},
         'D': {'outgoing':[],'incoming':['B','C']},
         'E': {'outgoing':['F'],'incoming':['C']},
         'F': {'outgoing':[],'incoming':['C','E']}
         }

print(topological_ordering(graph))