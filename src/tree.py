class TreeNode():
    def __init__(self, parent, value, index, children):
        self.parent = parent
        self.value = value
        self.index = index
        self.children = children

class Tree():
    def __init__(self, edges, node_values):
        self.edges = edges
        self.val_list = node_values
        root_value = self.val_list[self.get_root(self.edges)]
        root_index = self.get_root(self.edges)
        self.root = TreeNode(None, root_value, root_index, None)
    
    def get_children(self, target_index, edges):
        return [branch[1] for branch in edges if branch[0] == target_index]

    def get_parent(self, target_index, edges):
        for branch in edges:
            if branch[1] == target_index:
                return branch[0]

    def get_root(self, edges):
        for branch in edges:
            if self.get_parent(branch[0], edges) == None:
                return branch[0]

    def build_from_edges(self):
        current_nodes = [self.root]
        while len(current_nodes) != 0:
            all_children = []
            for node in current_nodes:
                node_children = self.get_children(node.index, self.edges)
                for i in range(len(node_children)):
                    node_children[i] = TreeNode(node, self.val_list[node_children[i]], node_children[i], None)
                node.children = node_children
                for i in node_children:
                    all_children.append(i)
            current_nodes = all_children
    
    def nodes_breadth_first(self):
        queue = [self.root]
        visited = []
        while len(queue) != 0:
            node = queue[0]
            visited.append(node)
            if node.children != None:
                for node_child in node.children:
                    queue.append(node_child)
            queue.remove(node)
        return visited
    
    def nodes_depth_first(self):
        stack = [self.root]
        visited = []
        while len(stack) != 0:
            top_node = stack[0]
            visited.append(top_node)
            if top_node.children != None:
                for node_child in top_node.children:
                    stack.insert(0, node_child)
            stack.remove(top_node)
        return visited

