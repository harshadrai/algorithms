def depth_first_search(graph,start_node,node_to_find,nodes_seen=None):
    if not nodes_seen:
        nodes_seen=[]
    nodes_seen.append(start_node)
    if start_node==node_to_find:
        return start_node
    else:
        for neighbor_node in graph[start_node]:
            if neighbor_node not in nodes_seen:
                node_returned=depth_first_search(graph,neighbor_node,node_to_find,nodes_seen)
                if node_returned:
                    return node_returned

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D','F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C','E'],
         'G': []}

print(depth_first_search(graph, 'A', 'E'))
print(depth_first_search(graph, 'A', 'G'))

