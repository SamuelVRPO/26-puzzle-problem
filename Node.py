from helper_functions import total_manhattan_dist

class Node:
    def __init__(self, state, action=None, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
    
    def __le__(self, other):
        return self.path_cost <= other.path_cost