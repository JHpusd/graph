class GraphNode():
    def __init__(self, index, value=None):
        self.index = index
        self.neighbors = []
        self.value = value

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

