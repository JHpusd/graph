import sys
sys.path.append('src')
from graph import *

class WeightedNode():
    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.neighbors = []
        self.previous = None
        self.d_val = 999999999999

class WeightedGraph():
    def __init__(self, weights, values):
        self.weights = weights
        self.values = values
        self.edges = [key for key in self.weights]
        index_list = []
        for pair in self.edges:
            index_list.append(pair[0])
            index_list.append(pair[1])
        self.nodes = [WeightedNode(i, self.values[i]) for i in range(max(index_list) + 1)]
    
    def construct_graph(self):
        for pair in self.edges: 
            self.nodes[pair[0]].neighbors.append(self.nodes[pair[1]])
            self.nodes[pair[1]].neighbors.append(self.nodes[pair[0]])
    
    def get_edge_weight(self, first_node, second_node):
        for edge in self.weights:
            if first_node.index in edge and second_node.index in edge:
                return self.weights[edge]
    
    def set_distance_and_previous(self, start_index):
        for node in self.nodes:
            node.previous = None
            node.d_val = 999999999999

        nodes_copy = [node for node in self.nodes]
        start_node = self.nodes[start_index]
        start_node.d_val = 0
        
        queue = [start_node]
        visited = []
        current_node = queue[0]
        while len(visited) < len(self.nodes):
            visited.append(current_node)
            nodes_copy.remove(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    weight = self.get_edge_weight(current_node, neighbor)
                    if current_node.d_val + weight < neighbor.d_val:
                        neighbor.d_val = current_node.d_val + weight
                    neighbor.previous = current_node
                    queue.append(neighbor)
            queue.remove(current_node)

            if len(nodes_copy) != 0:
                smallest_d_val = nodes_copy[0].d_val
                current_node = nodes_copy[0]
                for node in nodes_copy:
                    if node.d_val < smallest_d_val:
                        current_node = node
                        smallest_d_val = node.d_val
    
    def calc_distance(self, start_index, end):
        self.set_distance_and_previous(start_index)
        if self.nodes[end].d_val == None:
            return False
        return self.nodes[end].d_val
    
    def calc_shortest_path(self, start_index, end):
        self.set_distance_and_previous(start_index)
        new_edges = []
        for a,b in self.edges:
            if self.nodes[b].d_val - self.nodes[a].d_val == self.weights[(a,b)]:
                new_edges.append((a,b))
        demo_graph = Graph(new_edges)
        demo_graph.build_from_edges()
        return demo_graph.calc_shortest_path(start_index, end)


