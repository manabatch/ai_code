import numpy as np

class Node:
    def __init__(self, state, parent=None, action=None, level=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.level = level

def dfs(node, goal_state, depth, visited=set()):
    if np.array_equal(node.state, goal_state):
        return node
    if depth == 0:
        return None
    visited.add(tuple(node.state.ravel()))
    for action, new_state in get_successors(node.state):
        if tuple(new_state.ravel()) not in visited:
            child = Node(new_state, node, action, node.level + 1)
            result = dfs(child, goal_state, depth - 1, visited)
            if result is not None:
                return result
    return None

def solve_puzzle(initial_state, goal_state, max_depth):
    node = Node(initial_state)
    return dfs(node, goal_state, max_depth)

def get_successors(state):
    successors = []
    size = state.shape[0]
    blank_position = np.argwhere(state == 0)[0]
    for action in ['up', 'down', 'left', 'right']:
        new_position = np.array(blank_position)
        if action == 'up':
            if blank_position[0] > 0:
                new_position[0] -= 1
        elif action == 'down':
            if blank_position[0] < size - 1:
                new_position[0] += 1
        elif action == 'left':
            if blank_position[1] > 0:
                new_position[1] -= 1
        elif action == 'right':
            if blank_position[1] < size - 1:
                new_position[1] += 1
        if np.array_equal(new_position, blank_position):
            continue
        new_state = np.copy(state)
        new_state[blank_position[0], blank_position[1]] = state[new_position[0], new_position[1]]
        new_state[new_position[0], new_position[1]] = 0
        successors.append((action, new_state))
    return successors

def get_path(node):
    path = []
    while node is not None:
        path.append((node.state, node.action, node.level))
        node = node.parent
    path.reverse()
    return path


initial_state = np.array([[1, 0, 3], [4, 2, 5], [7, 8, 6]])
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

max_depth = 20
node = solve_puzzle(initial_state, goal_state, max_depth)
if node is not None:
    at = []
    path = get_path(node)
    for state, action, level in path:
        print("Level: ", level)
        at.append(action)
        print(action)
        print(state)
    print("Overall path is - ", at)
    print("Goal state is reached")
else:
    print("No solution found within the given depth limit.")
