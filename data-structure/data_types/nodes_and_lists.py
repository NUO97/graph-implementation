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


class NodeArray(object):

    def __init__(self, size):
        self.size = size
        PyArray = ctypes.py_object * size
        self._items = PyArray()
        self.count = 0
        self.clear(None)

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, data):
        self._items[index] = data

    def __iter__(self):
        return ArrayIterator(self._items)

    def __contains__(self, target):
        pass

    def search(self, target):
        pass

    def clear(self, value):
        for index in range(self.size):
            self._items[index] = value

    def add_node(self, data, index=None, edge=None):
        node = Node(data)
        if index:
            node.id = index
            self._items[index] = node
            self.count += 1
        elif self.count < self.size:
            node.id = self.count
            self._items[self.count] = node
            self.count += 1
        else:
            print "Array Resized"
            resize = self.size * 2
            n_arr = NodeArray(resize)
            n_arr.copy(self._items)
            self._items = n_arr
            self._items[self.count] = node
            node.id = self.count
            self.size = resize
            self.count += 1

    def full(self):
        return self.count == self.size

    def copy(self, arr):
        for index, item in enumerate(arr):
            self._items[index] = item

class ArrayIterator(object):

    def __init__(self, arr):
        self.array = arr
        self.current = 0

    def __iter__(self):
        return self

    def next(self):
        if self.current < len(self.array):
            output = self.array[self.current]
            self.current += 1
            return output
        else:
            return

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        return self.length

    def __contains__(self, target):
        return self.search(target)

    def search(self, target):
        current = self.head
        while current != None and current.data != target:
            current = current.next
        return current is not None

    def add_node(self, data, edge_reference=None):
        if edge_reference:
            node = LinkedListNode(data,edge_reference)
        else:
            node = LinkedListNode(data)
        if self.head == None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

class LinkedListIterator(object):

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def next(self):
        if self.current == None:
            return
        else:
            node = self.current
            self.current = self.current.next
            return node

class Stack(object):

    def __init__(self):
        self.top = None
        self.length = 0

    def __len__(self):
        return self.length

    def push(self,data):
        node = StackNode(data)
        if self.top == None:
            self.top = node
            self.length += 1
        else:
            node.prev = self.top
            self.top = node
            self.length += 1

    def pop(self):
        pop = self.top
        self.top = self.top.prev
        self.length -= 1
        return pop

    def peek(self):
        return self.top.data
