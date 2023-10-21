#A State represents a state within a Transition System
class State:
    labels: list[str] = []
    next_states = []
    
    def __init__(self, label_list: list[str], next_states = []):
        self.labels = label_list
        self.next_states = next_states

    def get_labels(self):
        return self.labels

    def set_next_states(self, next_states):
        self.next_states = next_states

    def get_next_states(self):
        return self.next_states
    
    def display(self):
        print(self.labels)
        print("Has the follwing succesors: ")
        print([state.get_labels() for state in self.next_states])

#A TransitionSystem represents a transition system, and contains the states of its initial states
class TransitionSystem:
    initial_states: list[State] = []

    def __init__(self, initial_states: list[State]):
        self.initial_states = initial_states

    def get_initial_states(self):
        return self.initial_states

    def add_initial_state(self, state: State):
        self.initial_states.append(state)