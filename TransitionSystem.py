#A node represents a state within a Transition System
class Node:
    labels: list[str] = []
    next_nodes = []
    
    def __init__(self, label_list: list[str], next_nodes = []):
        self.labels = label_list
        self.next_nodes = next_nodes

    def get_labels(self):
        return self.labels

    def set_next_nodes(self, next_nodes):
        self.next_nodes = next_nodes

    def get_next_nodes(self):
        return self.next_nodes
    
    def display(self):
        print(self.labels)
        print("Has the follwing succesors: ")
        print([node.get_labels() for node in self.next_nodes])

#A TransitionSystem represents a transition system, and contains the nodes of its initial states
class TransitionSystem:
    initial_nodes: list[Node] = []

    def __init__(self, initial_nodes: list[Node]):
        self.initial_nodes = initial_nodes

    def get_initial_nodes(self):
        return self.initial_nodes

    def add_initial_node(self, node: Node):
        self.initial_nodes.append(node)