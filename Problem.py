from State import State
# The Problem class contains all the methods necessary for the problem
# - Initial, Goal are the initial and goal states of the problem, see State class
# - Actions return the possible actions that can be performed given the current state
# - Action Cost just returns 1, this was in order to make the A* search look cleaner
# - Result takes the coordinates of the blank tile, finds the swap partner in the board,
#      swaps the partner and the blank tile in the board as well as coordinates.
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
    
    def action_cost(self, _state, _action, _s_prime):
        return 1
    
    def is_goal(self, state):
        return state.board == self.goal.board
    
    def result(self, state, action):
        s_prime = State(state.board, state.coordinates)
        # Obtain coordinates of blank tile
        blank_tile_coordinates = s_prime.coordinates[0]
        b_x, b_y, b_z = blank_tile_coordinates[0], blank_tile_coordinates[1], blank_tile_coordinates[2]
        if action == 'E':
            #find swap partner
            swap_partner = s_prime.board[b_z][b_y][b_x+1]
            #swap blank tile with partner in board
            s_prime.board[b_z][b_y][b_x] = swap_partner
            s_prime.board[b_z][b_y][b_x+1] = 0
            #swap coordinates
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