class GraphNode():
    def __init__(self, index, value=None):
        self.index = index
        self.neighbors = []
        self.value = value
        self.distance = None
        self.previous = None

class Graph():
    def __init__(self, edges):
        self.edges = edges
        index_list = []
        for pair in edges:
            index_list.append(pair[0])
            index_list.append(pair[1])
        self.nodes = [GraphNode(i) for i in range(max(index_list) + 1)]
    
    def build_from_edges(self):
        for pair in self.edges: 
            self.nodes[pair[0]].neighbors.append(self.nodes[pair[1]])
            self.nodes[pair[1]].neighbors.append(self.nodes[pair[0]])
    
    def nodes_breadth_first(self, first_node_index):
        queue = [self.nodes[first_node_index]]
        visited = []
        while len(queue) != 0:
            current_node = queue[0]
            visited.append(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
            queue.remove(current_node)
        return visited
    
    def nodes_depth_first(self, first_node_index):
        stack = [self.nodes[first_node_index]]
        visited = []
        while len(stack) != 0:
            current_node = stack[0]
            visited.append(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited and neighbor not in stack:
                    stack.insert(0, neighbor)
            stack.remove(current_node)
        return visited
    
    def set_breadth_first_distance_and_previous(self, starting_node):
        for node in self.nodes:
            node.distance = None
            node.previous = None

        first_node = self.nodes[starting_node]
        first_node.distance = 0

        queue = [first_node]
        visited = []
        while len(queue) != 0:
            current_node = queue[0]
            visited.append(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    neighbor.distance = current_node.distance + 1
                    neighbor.previous = current_node
            queue.remove(current_node)
    
    def calc_distance(self, start_node, end_node):
        self.set_breadth_first_distance_and_previous(start_node)
        return self.nodes[end_node].distance
    
    def calc_shortest_path(self, start_node, end_node):
        self.set_breadth_first_distance_and_previous(start_node)
        current_node = self.nodes[end_node]

        nodes = [current_node]
        while current_node.index != start_node:
            nodes.append(current_node.previous)
            current_node = current_node.previous
        return [node.index for node in nodes][::-1]

