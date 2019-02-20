# graph-implementation
Implementing knowledge space as a graph

Nodes
=====

Each node has 3 different attributes: .data, .id, .edges

1. data stores the information about the node (i.e concepts, subjects)
2. id stores an id number correponding to the index of the NodeArray where the node is stored
3. edge stores a doubly linked list with all its edges


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


