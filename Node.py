from helper_functions import total_manhattan_dist

# The Node class contains all the attributes necessary:
# - State is the current state of the game, see State class
# - Parent is the parent node of the current node
# - Action is the action that lead to the current state {E, W, N, S, U, D}
# - Path cost is the path cost of the current node
# The two functions are for the < and <= operators for comparison, disregard them

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