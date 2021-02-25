import numpy as np
import copy
import math

def karger_min_cut(nodes_and_edges):
    nodes=list(nodes_and_edges.keys())
    while len(nodes)>2:
        random_index=np.random.random_integers(0,len(nodes)-1)
        start_node=nodes[random_index]
        probable_dropouts=nodes_and_edges[start_node]
        collapsing_node_index=np.random.random_integers(0,len(probable_dropouts)-1)
        collapsing_node=probable_dropouts[collapsing_node_index]
        while collapsing_node in probable_dropouts:
            probable_dropouts.remove(collapsing_node)
        collapsing_node_edges=nodes_and_edges[collapsing_node]
        while start_node in collapsing_node_edges:
            collapsing_node_edges.remove(start_node)
        probable_dropouts.extend(collapsing_node_edges)
        nodes_and_edges.pop(collapsing_node)
        nodes=list(nodes_and_edges.keys())
        for node in nodes:
            while collapsing_node in nodes_and_edges[node]:
                nodes_and_edges[node][nodes_and_edges[node].index(collapsing_node)]=start_node
    return len(nodes_and_edges[start_node])


def find_min_cut(graph):
    min_cuts=math.inf
    for i in range(20):
        nodes_and_edges_copy=copy.deepcopy(graph)
        iteration_min_cut=karger_min_cut(nodes_and_edges_copy)
        if iteration_min_cut<min_cuts:
            min_cuts=iteration_min_cut
    return min_cuts

#a={1:[2,3,5],2:[1,4],3:[1,4,5],4:[2,3],5:[1,3]}
#find_min_cut(a) #should be 2