import queue
from helper_functions import get_initial_state, total_manhattan_dist
from helper_classes import Node, Problem

initial_state, goal_state = get_initial_state('test1.txt')

problem = Problem(initial_state, goal_state)

def expand(problem, node):
    s = node.state
    children = []
    for action in problem.actions(s):
        s_prime = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s_prime)
        child = Node(s_prime, action, node, cost)
        children.append(child)
    return children

def a_star_search(problem):
    node = Node(problem.initial)
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


print(a_star_search(problem))