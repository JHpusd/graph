class TreeNode():
    def __init__(self, parent, value, children):
        self.parent = parent
        self.value = value
        self.children = children

class Tree():
    def __init__(self, edges):
        self.edges = edges
        self.root = TreeNode(None, self.get_root(self.edges), None)
    
    def get_children(self, target, tree):
        result_list = []
        for branch in tree:
            if branch[0] == target:
                result_list.append(branch[1])
        return result_list

    def get_parents(self, target, tree):
        for branch in tree:
            if branch[1] == target:
                return branch[0]
            else:
                continue

    def get_root(self, tree):
        for branch in tree:
            if self.get_parents(branch[0], tree) == None:
                return branch[0]
            else:
                continue

    def make_child_list(self, node, edges):
        for i in range(len(child_list)):
            child_list[i] = TreeNode(node, child_list[i], None)
        return child_list

    def build_from_edges(self):
        current_nodes = [self.root]
        while len(current_nodes) != 0:
            all_children = []
            for node in current_nodes:
                node_children = self.get_children(node.value, self.edges)
                for i in range(len(node_children)):
                    node_children[i] = TreeNode(node, node_children[i], None)
                node.children = node_children
                for i in node_children:
                    all_children.append(i)
            current_nodes = list(all_children)