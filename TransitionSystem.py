class TransitionSystem:
    initial_nodes = []

    def get_initial_nodes(self):
        return self.initial_nodes

    def __init__(self):
        pass
        
class Node:
    label = ""
    next_nodes = []
    
    def get_next_nodes(self):
        return self.next_nodes
    