class QueueElement:
    def __init__(self,value=None,next=None,prev=None):
        self.value=value
        self.next=next
        self.prev=prev

class Queue:
    def __init__(self,element=None):
        self.head=element
        self.tail=element
    def enqueue(self,element):
        if not isinstance(element,QueueElement):
            element=QueueElement(value=element)
        if not self.head:
            self.head=element
            self.tail=element
        else:
            last_element=self.tail
            last_element.next=element
            element.prev=last_element
            self.tail=element
    def dequeue(self):
        exiting_element=self.head
        self.head=exiting_element.next
        if not self.head:
            self.tail=None
        else:
            exiting_element.next.prev=None
        return exiting_element.value
    def is_empty(self):
        if self.head:
            return False
        else:
            return True

def breadth_first_search(graph,element):
    graph_nodes=list(graph.keys())
    for s in graph_nodes:
        elements_seen=[s]
        q=Queue()
        q.enqueue(s)
        while not q.is_empty():
            current_node=q.dequeue()
            if current_node==element:
                return graph[current_node]
            else:
                for neighboring_node in graph[current_node]:
                    if neighboring_node not in elements_seen:
                        q.enqueue(neighboring_node)

