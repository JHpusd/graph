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

assert graph.calc_distance(0,4) == 2
assert graph.calc_distance(5,2) == 3
assert graph.calc_distance(0,5) == 3
assert graph.calc_distance(4,1) == 1
assert graph.calc_distance(3,3) == 0

assert graph.calc_shortest_path(0,4) == [0,1,4]
assert graph.calc_shortest_path(5,2) == [5,4,1,2]
assert graph.calc_shortest_path(0,5) == [0,1,4,5]
assert graph.calc_shortest_path(4,1) == [4,1]
assert graph.calc_shortest_path(3,3) == [3]


