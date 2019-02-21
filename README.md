# graph-implementation
Implementing knowledge space as a graph

Nodes
=====

Each node has 3 different attributes: .data, .id, .edges

1. data stores the information about the node (i.e concepts, subjects)
2. id stores an id number correponding to the index of the NodeArray where the node is stored
3. edge stores a doubly linked list with all its edges

```python
>>> n = Node("math")

>>> n.data
>>> 'math'

>>> n.id

>>> n.edges
>>> <__main__.LinkedList at 0x9a72e4k>
```

NodeArray
=========

NodeArray assigns ID to each nodes using the array index, when array is full, a new array twice the size of the original one is created and copies the content of the original array into the new array.  

```python
>>> arr = NodeArray(size=1)

>>> a.add_node('math')

>>> a[0].data
>>> 'math'

>>> a[0].id
>>> 0

>>> a.add_node('physics')
Array Resized

>>> a.size
>>> 2

>>> a[1].data
>>> 'physics'

>>> a[1].id
>>> 1
```
Linked List Nodes
=================

The graph's nodes are connected by edges. An edge is created by adding a linked list node to a graph node's edge list. Each linked list node has three attributes: .data, .prev, .next, and .edge_reference       

1. .data contains the id number of the destination node of the edge  
2. .prev is the linked list reference of the previous node  
3. .next is the linked list reference of the next node  
4. .edge_reference points to an edge object   


```python
>>> l = LinkedListNode("2019",edge_reference="SomeEdge")

>>> l.data
>>> '2019'

>>> l.prev

>>> l.next

>>> l.edge_reference
>>> 'SomeEdge'
```

Edges
=====

Each edge object has three attributes: .data, .source, .target 

1. .data stores anydata contained in the edge (assigned upon instantiation)  
2. .source is a reference to linked list nodes in the edge list (from)  
3. .target is a reference to linked list nodes in the edge list (to)  

```python
>>> e = Edge("Question: What's the meaning of area under the curve? Answer: Integral")

>>> e.data
>>> 'Question: What's the meaning of area under the curve? Answer: Integral'

>>> e.source

>>> e.target
```
Graph
=====

Graph is constructed with all the above data structures and provides the following attributes/methods:

1. size stores the size of the graph  
2. node_dict contains a dictionary of node id and data
3. create_node method increments the graph size by 1 and adds the node to the nodearray  
4. create_edge method creates an edge object and adds each other to the edge attribute of each node    
5. adjacent_nodes method returns boolean value and determines if two nodes are adjacent  
6. search_edge method find and returns a reference to an edge object  
7. destroy_node removes the node from the nodearray  
8. destroy_edge removes the edge object 
9. is_connected returns a boolean value that determines if the graph is connected  
10. traversal method visits all nodes and edges  
11. breadth_search method uses BFS to traverse through the entire graph  
12. neighbors_traversal finds all neighbors of a node to a certain degree of separation  
13. generate_random method creates a random graph with a certain number of nodes and a probability that the nodes are connected  


### Create and Destroy Nodes

```python

>>> G = AGraph()

>>> G.create_node("math")

>>> G.nodes[0].data
>>> 'math'

>>> G.nodes[0].id
>>> 0

>>> G.create_node("physics")

>>> G.nodes[1].data
>>> 'physics'

>>> G.nodes[1].id
>>> 1

>>> G.size
>>> 2

>>> G.node_dict
>>> {0: 'math', 1: 'physics'}

>>> G.create_edge("Question: xxx. Answer: xxx",0,1)

>>> G.adjacent(0,1)
>>> True

>>> G.nodes[0].neighbors
>>> set([1])

>>> G.nodes[1].neighbors
>>> set([0])

>>> G.destroy_node(0)

>>> G.nodes[1].neighbors
>>> set([])
```

### Generate a Random Graph 

```python

>>> G = AGraph.generate_random(10, 0.4)

>>> G.nodes[0].neighbors
>>> set([9, 5, 2, 3])

>>> G.nodes[8].neighbors
>>> set([7, 3, 0, 5])

>>> G.destroy_node(0)

>>> G.nodes[8].neighbors
>>> set([7, 3, 5])

>>> G.nodes[1].neighbors
>>> set([2, 3, 4, 5])
```

### Traverse the graph



### Neighbors Traversal




