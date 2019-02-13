import random
import itertools
from data_types.nodes_and_lists import *

class AGraph(object):
    """An adjacency list style graph with node creation, deletion, edge creation and deletion,
    Added edge search and adjacency search, and graph traversal  """

    @staticmethod
    def generate_random(size, prob):
        """ Generate random graphs for testing"""
        G = AGraph(size)
        for index in range(size):
            G.create_node(index)
        edges = itertools.combinations(range(size),2)
        for edge in edges:
            if random.random() < prob:
                G.create_edge("edge",edge[0],edge[1])
        return G

    def __init__(self,size=None):
        if size:
            self.nodes = NodeArray(size)
        else:
            self.nodes = NodeArray(1000)
        self.size = 0

    def __len__(self):
        return self.size

    def _get_node_dict(self):
        nodes = {}
        for index in range(self.nodes.count):
            node = self.nodes[index]
            nodes[node.id] = node.data
        return nodes

    node_dict = property(_get_node_dict)

    def create_node(self, data):
        self.size += 1
        self.nodes.add_node(data)

    def create_edge(self, data, source, target):
        node1 = self.nodes[source]
        node2 = self.nodes[target]
        edge = Edge(data)
        node1.edges.add_node(target, edge_reference=edge)
        node2.edges.add_node(source, edge_reference=edge)
        edge.source = node1.edges.tail
        edge.target = node2.edges.tail

    def adjacent_nodes(self, node1, node2):
        for edge in self.nodes[node1].edges:
            if edge.data == node2:
                return True
        return False

    def search_edge(self, source, target):
        for node in self.nodes[source].edges:
            if node.data == target:
                return node.edge_reference

    def destroy_node(self, index):
        for node in self.nodes[index].edges:
            self.destroy_edge(node.edge_reference)
        self.nodes[index] = None
        self.size -= 1

    def destroy_edge(self, edge):
        self._reference_node_destructor(edge.target,edge.source.data)
        self._reference_node_destructor(edge.source,edge.target.data)
        edge.target = None
        edge.source = None

    def _reference_node_destructor(self, llist_node, target_index):
        if llist_node is self.nodes[target_index].edges.head:
            self.nodes[target_index].edges.head = self.nodes[target_index].edges.head.next
            llist_node.next = None
        elif llist_node is self.nodes[target_index].edges.tail:
            self.nodes[target_index].edges.head = self.nodes[target_index].edges.head.next
            llist_node.prev = None
        else:
            llist_node.prev.next = llist_node.next
            llist_node.next.prev = llist_node.prev
            llist_node.prev = None
            llist_node.next = None

    def is_connected(self):
        return self.traversal(0)

    def traversal(self, start):
        node = self.nodes[start]
        visited = NodeArray(size=self.size)
        visited.add_node(True, index=node.id)
        stack = Stack()
        stack.push(node.id)
        print "%i : %s" % (node.id,node.data)
        while not visited.full():
            if node._valid_neighbors(visited):
                for neighbor in node.edges:
                    if not visited[neighbor.data]:
                        node = self.nodes[neighbor.data]
                        stack.push(neighbor.data)
                        visited.add_node(True, index=neighbor.data)
                        print "%i : %s" % (node.id,node.data)
            else:
                stack.pop()
                if len(stack) == 0:
                    return False
                else:
                    node = self.nodes[stack.peek()]
        return True

    def breadth_search(self, start, finish):
        node = self.nodes[start]
        stack = Stack()
        stack.push(node.id)
        visited = NodeArray(size=self.size)
        visited[node.id] = node
        while True:
            if node.id == finish:
                for x in range(len(stack)):
                    pop = stack.pop()
                    print pop.data,
                print "\n"
                return True
            elif node._valid_neighbors(visited):
                for neighbor in node.edges:
                    if not visited[neighbor.data]:
                        node = self.nodes[neighbor.data]
                        stack.push(neighbor.data)
                        visited[neighbor.data] = node
            else:
                stack.pop()
                if len(stack) == 0:
                    return False
                else:
                    node = self.nodes[stack.peek()]

    def neighbors_traversal(self,start,degree_sep):
        node = self.nodes[start]
        visited = NodeArray(size=self.size)
        visited.add_node(True,index=node.id)
        neighbors = node.neighbors
        neighbors.update([node.id])
        current_neighbors = neighbors
        for i in range(degree_sep-1):
            local_neighbors = set()
            for neighbor in current_neighbors:
                if not visited[neighbor]:
                    local_neighbors.update(self.nodes[neighbor].neighbors)
                    visited.add_node(True,index=neighbor)
            neighbors.update(local_neighbors)
            current_neighbors = local_neighbors
        return neighbors

    # Still in progress, didn't finish debugging

    # def recursive_neighbors_traversal(self, start, degree_sep, visited=None):
    #
    #     node = self.nodes[start]
    #     if visited ==  None:
    #         visited = NodeArray(size=self.size)
    #     visited.add_node(True, index=node.id)
    #     neighbors = set(node.neighbors)
    #     neighbors.update([node.id])
    #     if degree_sep > 1:
    #         for neighbor in node.edges:
    #             if not visited[neighbor.data]:
    #                 n_neighbors = self.recursive_neighbors_traversal(neighbor.data, degree_sep-1,
    #                                                         visited=visited)
    #                 neighbors.update(n_neighbors)
    #     return neighbors

    # def recursive_breadth_search(self, start, finish, path=None):
    #     if not path:
    #         path = LinkedList()
    #     node = self.nodes[start]
    #     path.add_node(start)
    #     if start == finish:
    #         for node in path:
    #             print node.data,
    #         print "\n"
    #         return True
    #     for neighbor in node.edges:
    #         if neighbor.data not in path:
    #             n_path = self.recursive_breadth_search(neighbor.data,finish,path)
    #             if n_path:
    #                 return True
    #     return False

    # def recursive_traversal(self, start, visited=None):
    #     node = self.nodes[start]
    #     if visited == None:
    #         visited = NodeArray(size=self.size)
    #         print "%i : %s" % (node.id, node.data)
    #     visited.add_node(True, index=node.id)
    #     if visited.full():
    #         return True
    #     elif node._valid_neighbors(visited):
    #         for neighbor in node.edges:
    #             if not visited[neighbor.data]:
    #                 print "%i : %s" % (self.nodes[neighbor.data].id,self.nodes[neighbor.data].data)
    #                 n_traversal = self.recursive_traversal(neighbor.data,visited=visited)
    #                 if n_traversal:
    #                     return True
    #     return False
