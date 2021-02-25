import copy

class QueueElement:
    def __init__(self,value=None,next=None,prev=None):
        self.value=value
        self.next=None
        self.prev=None

class Queue:
    def __init__(self,element=None):
        if not isinstance(element,QueueElement):
            element=QueueElement(element)
        self.head=element
        self.tail=element
    def enqueue(self,element):
        if not isinstance(element,QueueElement):
            element=QueueElement(element)
        if not self.head:
            self.head=element
            self.tail=element
        else:
            element.prev=self.tail
            self.tail=element
            element.prev.next=element
    def dequeue(self):
        exiting_element=self.head
        self.head=exiting_element.next
        if not self.head:
            self.tail=None
        else:
            self.head.prev=None
        exiting_element.next=None
        return exiting_element
    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

def shortest_path(graph,start_node,end_node):
    nodes_seen=[start_node]
    path={}
    path_distance={}
    q=Queue(start_node)
    path_distance[start_node]=0
    path[start_node]=[start_node]
    while not q.is_empty():
        current_node=q.dequeue().value
        if current_node==end_node:
            return path[current_node],path_distance[current_node]
        else:
            for neighbor_node in graph[current_node]:
                if neighbor_node not in nodes_seen:
                    nodes_seen.append(neighbor_node)
                    q.enqueue(neighbor_node)
                    path_distance[neighbor_node]=path_distance[current_node]+1
                    path[neighbor_node]=copy.deepcopy(path[current_node])
                    path[neighbor_node].append(neighbor_node)


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D','F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C','E']}

print(shortest_path(graph, 'A', 'E'))