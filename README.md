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
>>> <__main__.LinkedList at 0x8b92e4c>
```

NodeArray
=========

NodeArray assigns ID to each nodes using the array index, when array is full, a new array twice the size of the original one is created and copies the content of the original array into the new array.

Linked List Nodes
=================

The graph's nodes are connected by edges. An edge is created by adding a linked list node to a graph node's edge list. Each linked list node has three attributes: .data, .prev, .next, and .edge_reference       

1. .data contains the id number of the destination node of the edge  
2. .prev is the linked list reference of the previous node  
3. .next is the linked list reference of the next node  
4. .edge_reference points to an edge object   


Edges
=====

Each edge object has three attributes: .data, .source, .target 

1. .data stores anydata contained in the edge (assigned upon instantiation)  
2. .source is a reference to linked list nodes in the edge list (from)  
3. .target is a reference to linked list nodes in the edge list (to)

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


Create and Destroy Nodes
========================



Generate a Random Graph 
=======================


Traverse the graph
==================


Neighbors Traversal
===================



