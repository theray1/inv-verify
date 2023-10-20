class TransitionSystem:
    initial_nodes = []

    def get_initial_nodes(self):
        return self.initial_nodes

    def add_initial_node(self, node: Node):
        self.initial_nodes.append(node)

    def __init__(self):
        pass
        
class Node:
    labels = []
    next_nodes = []
    
    def get_next_nodes(self):
        return self.next_nodes
    