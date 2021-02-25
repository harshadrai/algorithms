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

def breadth_first_search(graph,start_node,nodes_seen):
    nodes_seen.append(start_node)
    q=Queue(start_node)
    connected_components=[]
    while not q.is_empty():
        current_node=q.dequeue().value
        connected_components.append(current_node)
        for neighbor_node in graph[current_node]:
            if neighbor_node not in nodes_seen:
                nodes_seen.append(neighbor_node)
                q.enqueue(neighbor_node)
    return connected_components

def connected_components(graph):
    nodes_seen=[]
    connected_components=[]
    for node in list(graph.keys()):
        if not node in nodes_seen:
            connected_components.append(breadth_first_search(graph,node,nodes_seen))
    return connected_components


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D',],
         'D': ['C'],
         'E': [],
         'F': []}

print(connected_components(graph))
