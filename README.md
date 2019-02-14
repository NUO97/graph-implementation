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

Linked list nodes stores the edges



To Be Continued, I'll add examples of how to access each attributes and methods later
====================================================================


