import sys
sys.path.append('src')
from directed_graph import *

edges = [(0,1),(1,2),(3,1),(4,3),(1,4),(4,5),(3,6)]
directed_graph = DirectedGraph(edges)
directed_graph.build_from_edges()


assert [[child.index for child in node.children] for node in directed_graph.nodes] == [
    [1], [2,4], [], [1,6], [3,5], [], []]
assert [[parent.index for parent in node.parents] for node in directed_graph.nodes] == [
    [], [0,3], [1], [4], [1], [4], [3]]

assert [node.index for node in directed_graph.nodes_breadth_first(4)] == [
    4, 3, 5, 1, 6, 2]
assert [node.index for node in directed_graph.nodes_depth_first(4)] == [
    4, 5, 3, 6, 1, 2]

assert directed_graph.calc_distance(0,3) == 3
assert directed_graph.calc_distance(3,5) == 3
assert directed_graph.calc_distance(0,5) == 3
assert directed_graph.calc_distance(4,1) == 2
assert not directed_graph.calc_distance(2,4)

assert directed_graph.calc_shortest_path(0,3) == [0,1,4,3]
assert directed_graph.calc_shortest_path(3,5) == [3,1,4,5]
assert directed_graph.calc_shortest_path(0,5) == [0,1,4,5]
assert directed_graph.calc_shortest_path(4,1) == [4,3,1]
assert not directed_graph.calc_shortest_path(2,4)

