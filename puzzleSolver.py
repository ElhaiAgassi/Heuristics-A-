from queue import PriorityQueue
import copy
from collections import defaultdict

def heuristic(state):
    # Calculate the estimated moves needed to consolidate each color into one tube.
    color_locations = defaultdict(list)
    for index, tube in enumerate(state):
        for color in tube:
            color_locations[color].append(index)

    moves = 0
    for color, locations in color_locations.items():
        if len(locations) > 1:
            # Simplified heuristic: count of tubes containing the color minus one times the average distance between tubes
            average_distance = sum(abs(loc - locations[0]) for loc in locations[1:]) / len(locations)
            moves += (len(locations) - 1) * average_distance
    return moves

def reconstruct_path(came_from, current_tuple):
    # "Reconstruct the path from start to goal.
    total_path = [current_tuple]
    seen = {current_tuple}

    while current_tuple in came_from:
        current_tuple = came_from[current_tuple]
        if current_tuple in seen:
            raise Exception("Loop detected in path reconstruction.")
        seen.add(current_tuple)
        total_path.append(current_tuple)

    total_path.reverse()
    total_path = [list(map(list, state)) for state in total_path]
    return total_path


def is_goal(state, size):
    # Check if all tubes are sorted or empty.
    for tube in state:
        if 0 < len(tube) and len(set(tube)) != 1:
            return False
    return True


def possible_moves(state, size):
    # Generate all possible valid moves.
    moves = []
    for i, src in enumerate(state):
        if len(src) == 0:
            continue  # Can't move from an empty tube
        src_color = src[-1]  # Color to move
        for j, dst in enumerate(state):
            if i != j and (len(dst) == 0 or (dst[-1] == src_color and len(dst) < size)):
                # Valid move: empty or matching color and not full
                new_state = copy.deepcopy(state)
                new_state[j].append(new_state[i].pop())  # Move color
                moves.append(new_state)
    return moves


def solve_puzzle(initial_state, size):
    # Optimized A* algorithm with consistent type handling for state.
    # Ensure the initial state is in the correct format
    initial_tuple = tuple(tuple(tube) for tube in initial_state)

    open_set = PriorityQueue()
    open_set.put((0, initial_tuple))
    came_from = {}
    g_score = {initial_tuple: 0}
    f_score = {initial_tuple: heuristic(initial_state)}
    visited = {initial_tuple}

    while not open_set.empty():
        _, current_tuple = open_set.get()

        # Convert current state from tuple back to list for processing
        current = [list(tube) for tube in current_tuple]

        if is_goal(current, size):
            # Convert back to tuple for consistent handling in reconstruct_path
            path = reconstruct_path(came_from, tuple(map(tuple, current)))
            return len(path) - 1, len(visited), path

        for move in possible_moves(current, size):
            move_tuple = tuple(map(tuple, move))
            tentative_g_score = g_score[current_tuple] + 1
            if move_tuple not in g_score or tentative_g_score < g_score[move_tuple]:
                came_from[move_tuple] = current_tuple
                g_score[move_tuple] = tentative_g_score
                f_score[move_tuple] = tentative_g_score + heuristic(move)
                if move_tuple not in visited:
                    open_set.put((f_score[move_tuple], move_tuple))
                    visited.add(move_tuple)

    return None, 0, []  # No solution found
