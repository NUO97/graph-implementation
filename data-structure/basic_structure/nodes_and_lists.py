import ctypes

class Node(object):

    def __init__(self, data):
        self.data = data
        self.id = None
        self.edges = LinkedList()

    def _get_neighbors(self):
        neighbors = set()
        for neighbor in self.edges:
            neighbors.update([neighbor.data])
        return neighbors

    neighbors = property(_get_neighbors)

    def _valid_neighbors(self, visited):
        for neighbor in self.neighbors:
            if not visited[neighbor]:
                return True
        return False

class LinkedListNode(object):
    def __init__(self, data, edge_reference=None):
        self.data = data
        self.edge_reference = edge_reference
        self.prev = None
        self.next = None

class StackNode(object):

    def __init__(self,data):
        self.data = data
        self.prev = None

class Edge(object):

    def __init__(self, data):
        self.data = data
        self.source = None
        self.target = None
