# Samuel Vieira Restrepo -- sv2657@nyu.edu
from copy import deepcopy
import queue
from helper_functions import get_initial_state, total_manhattan_dist
from Node import Node
from Problem import Problem

# This program contains the A* Search algorithm for the 26-Puzzle problem
# To run this program, change the name of the file on the get_initial_state() below
# Keep in mind the program will delete the result file before each run
initial_state, goal_state = get_initial_state('input1.txt')

problem = Problem(initial_state, goal_state)

nodes_generated = 0

# The expand, a_star_search functions are the ones we saw in class and were implemented
#   as close to that example as possible.
def expand(problem, node):
    global nodes_generated 
    s = node.state
    children = []
    for action in problem.actions(s):
        s_prime = problem.result(deepcopy(s), action)
        cost = node.path_cost + problem.action_cost(s, action, s_prime)
        child = Node(s_prime, action, node, cost)
        children.append(child)

    nodes_generated += len(children)
    return children

def a_star_search(problem):
    global nodes_generated 
    node = Node(problem.initial)
    nodes_generated = 1
    frontier = queue.PriorityQueue()
    frontier.put((total_manhattan_dist(node.state, problem.goal), node))
    reached = {str(problem.initial.board): node}
    while not (frontier.qsize == 0):
        node = frontier.get()[1]
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            s = child.state
            if str(s.board) not in reached or child.path_cost < reached[str(s.board)].path_cost:
                reached[str(s.board)] = child
                frontier.put((total_manhattan_dist(child.state, problem.goal), child))  
    return None

g1 = a_star_search(problem)

# The lines below populate the result file with the additional information.

result_file = open('result.txt', 'a')
depth = 0
moves = queue.LifoQueue()
f_values = queue.LifoQueue()
f_values.put(g1.path_cost + total_manhattan_dist(g1.state, problem.goal))
# Here we get all the moves in the optimal solution as well as the f() values for the nodes
while g1.parent != None:
    depth += 1
    moves.put(g1.action)
    g1 = g1.parent
    f_values.put(g1.path_cost + total_manhattan_dist(g1.state, problem.goal))

# Here write the depth, nodes generated, moves and f() values to the result file.
result_file.write('\n\n')
result_file.write(str(depth))
result_file.write('\n')
result_file.write(str(nodes_generated))
result_file.write('\n')
for i in range(depth):
    result_file.write(moves.get())
    result_file.write(" ")
result_file.write('\n')
for i in range(depth + 1):
    result_file.write(str(f_values.get()))
    result_file.write(" ")