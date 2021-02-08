class GraphNode():
    def __init__(self, index, value=None):
        self.index = index
        self.children = []
        self.parents = []
        self.value = value
        self.distance = None
        self.previous = None

class DirectedGraph():
    def __init__(self, edges):
        self.edges = edges
        index_list = []
        for pair in edges:
            index_list.append(pair[0])
            index_list.append(pair[1])
        self.nodes = [GraphNode(i) for i in range(max(index_list) + 1)]
    
    def build_from_edges(self):
        for pair in self.edges:
            self.nodes[pair[0]].children.append(self.nodes[pair[1]])
            self.nodes[pair[1]].parents.append(self.nodes[pair[0]])
    
    def nodes_breadth_first(self, first_node_index):
        queue = [self.nodes[first_node_index]]
        visited = []
        while len(queue) != 0:
            current_node = queue[0]
            visited.append(current_node)
            for child in current_node.children:
                if child not in visited and child not in queue:
                    queue.append(child)
            queue.remove(current_node)
        return visited
    
    def nodes_depth_first(self, first_node_index):
        stack = [self.nodes[first_node_index]]
        visited = []
        while len(stack) != 0:
            current_node = stack[0]
            visited.append(current_node)
            for child in current_node.children:
                if child not in visited and child not in stack:
                    stack.insert(0, child)
            stack.remove(current_node)
        return visited
    
    def set_breadth_first_distance_and_previous(self, starting_node_index):
        for node in self.nodes:
            node.distance = None
            node.previous = None

        first_node = self.nodes[starting_node_index]
        first_node.distance = 0

        queue = [first_node]
        visited = []
        while len(queue) != 0:
            current_node = queue[0]
            visited.append(current_node)
            for child in current_node.children:
                if child not in visited and child not in queue:
                    queue.append(child)
                    child.distance = current_node.distance + 1
                    child.previous = current_node
            queue.remove(current_node)
    
    def calc_distance(self, start_node, end_node):
        self.set_breadth_first_distance_and_previous(start_node)
        if self.nodes[end_node].distance == None:
            return False
        return self.nodes[end_node].distance
    
    def calc_shortest_path(self, start_node, end_node):
        self.set_breadth_first_distance_and_previous(start_node)
        current_node = self.nodes[end_node]
        if current_node.distance == None:
            return False

        node_indices = [current_node.index]
        while current_node.index != start_node:
            node_indices.append(current_node.previous.index)
            current_node = current_node.previous
        return node_indices[::-1]
