class TransitionSystem:
    initial_nodes = {}

    def get_initial_nodes(self):
        return self.initial_nodes

    class Node:
        label = ""
        next_nodes = []

    def __init__(self):
        pass
        
