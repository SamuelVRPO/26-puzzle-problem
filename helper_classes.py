class Node:
    def __init__(self, state, action=None, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
    
    def actions(self, state):
        possible_actions = ['E', 'W', 'N', 'S', 'U', 'D']
        blank_tile_coordinates = state.coordinates[0]
        if blank_tile_coordinates[0] == 0:
            possible_actions.remove('W')
        elif blank_tile_coordinates[0] == 2:
            possible_actions.remove('E')
        if blank_tile_coordinates[1] == 0:
            possible_actions.remove('N')
        elif blank_tile_coordinates[1] == 2:
            possible_actions.remove('S')
        if blank_tile_coordinates[2] == 0:
            possible_actions.remove('U')
        elif blank_tile_coordinates[2] == 2:
            possible_actions.remove('D')
        return possible_actions
    
    def action_cost(self, state, action, s_prime):
        return 1
    
    def is_goal(self, state):
        return state.board == self.goal.board
    
    def result(self, state, action):
        s_prime = State(state.board, state.coordinates)
        blank_tile_coordinates = s_prime.coordinates[0]
        b_x, b_y, b_z = blank_tile_coordinates[0], blank_tile_coordinates[1], blank_tile_coordinates[2]
        if action == 'E':
            swap_partner = s_prime.board[b_z][b_y][b_x+1]
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z][b_y][b_x+1] = 0
            s_prime.coordinates[0], s_prime.coordinates[swap_partner] = s_prime.coordinates[swap_partner], s_prime.coordinates[0]
        elif action == 'W':
            swap_partner = s_prime.board[b_z][b_y][b_x-1]
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z][b_y][b_x-1] = 0
            s_prime.coordinates[0], s_prime.coordinates[swap_partner] = s_prime.coordinates[swap_partner], s_prime.coordinates[0]
        elif action == 'N':
            swap_partner = s_prime.board[b_z][b_y-1][b_x]
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z][b_y-1][b_x] = 0
            s_prime.coordinates[0], s_prime.coordinates[swap_partner] = s_prime.coordinates[swap_partner], s_prime.coordinates[0]
        elif action == 'S':
            swap_partner = s_prime.board[b_z][b_y+1][b_x]
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z][b_y+1][b_x] = 0
            s_prime.coordinates[0], s_prime.coordinates[swap_partner] = s_prime.coordinates[swap_partner], s_prime.coordinates[0]
        elif action == 'U':
            swap_partner = s_prime.board[b_z-1][b_y][b_x]
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z-1][b_y][b_x] = 0
            s_prime.coordinates[0], s_prime.coordinates[swap_partner] = s_prime.coordinates[swap_partner], s_prime.coordinates[0]
        elif action == 'D':
            swap_partner = s_prime.board[b_z+1][b_y][b_x]
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z+1][b_y][b_x] = 0
            s_prime.coordinates[0], s_prime.coordinates[swap_partner] = s_prime.coordinates[swap_partner], s_prime.coordinates[0]
        return s_prime

class State:
    def __init__(self, board, coordinates):
        self.board = board
        self.coordinates = coordinates