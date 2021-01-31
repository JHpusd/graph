import sys
sys.path.append('src')
from graph import *

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
graph = Graph(edges)
graph.build_from_edges()

bf = graph.nodes_breadth_first(2)
assert [node.index for node in bf] == [2,1,0,3,4,5]

df = graph.nodes_depth_first(2)
assert [node.index for node in df] == [2,1,4,5,3,0]
