from graph import AGraph

# G = AGraph()
#
# G.create_node("Math")
#
# print(G.nodes[0].data)
#
# print(G.size)


G = AGraph.generate_random(10, 0.3)

print(G.nodes[1].data)
