import numpy as np
from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h

def solve_puzzle(initial_state, goal_state):
    open_list = deque([Node(initial_state, h=heuristic(initial_state, goal_state))])
    closed_list = set()
    while open_list:
        node = open_list.popleft()
        if node.state.tolist() == goal_state.tolist():
            return get_path(node)
        closed_list.add(tuple(node.state.ravel()))
        for action, new_state in get_successors(node.state):
            if tuple(new_state.ravel()) not in closed_list:
                child_g = node.g + 1
                child_h = heuristic(new_state, goal_state)
                child = Node(new_state, node, action, child_g, child_h)
                insert_node(child, open_list)
    return None

def insert_node(node, open_list):
    for i, n in enumerate(open_list):
        if node.f() < n.f():
            open_list.insert(i, node)
            return
    open_list.append(node)

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

def heuristic(state, goal_state):
    return np.sum(state != goal_state)

def get_path(node):
    path = []
    while node is not None:
        path.append((node.state, node.action, node.h, node.f()))
        node = node.parent
    path.reverse()
    return path

# initial_state = np.array([[1, 0, 3], [4, 2, 5], [7, 8, 6]])
initial_state = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

path = solve_puzzle(initial_state, goal_state)
if path is not None:
    for state, action, h, f in path:
        print(action)
        print(state)
        print("Heuristic value:", h)
        print("f(x) value:", f)
else:
    print('No solution found.')
