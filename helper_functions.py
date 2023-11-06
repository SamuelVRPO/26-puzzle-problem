from helper_classes import State

def get_initial_state(problem):
    problem_file = open('test1.txt', 'r')
    initial_board = []
    goal_board = []
    grid_level = []

    for line in problem_file:
        string_line = line.rstrip('\n').split(' ')
        if string_line == ['']:
            continue
        level_row = []
        if len(grid_level) == 3:
            if len(initial_board) == 3:
                goal_board.append(grid_level)
            else:
                initial_board.append(grid_level)
            grid_level = []
        if len(grid_level) < 3:
            for item in string_line:
                level_row.append(int(item))
            grid_level.append(level_row)
    goal_board.append(grid_level)

    initial_mp = {}
    z = 0
    for level in initial_board:
        y = 0
        for row in level:
            x = 0
            for el in row:
                initial_mp[el] = [x, y, z]
                x += 1
            y += 1
        z += 1
    
    goal_mp = {}
    z = 0
    for level in goal_board:
        y = 0
        for row in level:
            x = 0
            for el in row:
                goal_mp[el] = [x, y, z]
                x += 1
            y += 1
        z += 1
    
    initial_state = State(initial_board, initial_mp)
    goal_state = State(goal_board, goal_mp)
    return initial_state, goal_state

def total_manhattan_dist(curr_state, goal_state):
    total_manhattan_dist = 0
    for i in range(1, 27):
        tile_current_pos = curr_state.coordinates[i]
        tile_goal_pos = goal_state.coordinates[i]
        total_manhattan_dist += abs(tile_current_pos[0] - tile_goal_pos[0]) + abs(tile_current_pos[1] - tile_goal_pos[1]) + abs(tile_current_pos[2] - tile_goal_pos[2])
    return total_manhattan_dist