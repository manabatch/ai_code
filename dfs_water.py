# This function checks if the current state is already visited or not
def is_visited(state, visited):
    for i in visited:
        if i == state:
            return True
    return False

# This function checks if the current state is the goal state or not
def is_goal(state, goal):
    if state[0] == goal[0] and state[1] == goal[1]:
        return True
    else:
        return False

# This function performs DFS algorithm to find the solution
def dfs(current, goal, jug1_cap, jug2_cap, visited):
    if is_goal(current, goal):
        return current,visited
    visited.append(current)
    a, b = current
    # fill jug 1
    if a < jug1_cap and not is_visited((jug1_cap, b), visited):
        result = dfs((jug1_cap, b), goal, jug1_cap, jug2_cap, visited)
        if result is not None:
            return result
    # fill jug 2
    if b < jug2_cap and not is_visited((a, jug2_cap), visited):
        result = dfs((a, jug2_cap), goal, jug1_cap, jug2_cap, visited)
        if result is not None:
            return result
    # empty jug 1
    if a > 0 and not is_visited((0, b), visited):
        result = dfs((0, b), goal, jug1_cap, jug2_cap, visited)
        if result is not None:
            return result
    # empty jug 2
    if b > 0 and not is_visited((a, 0), visited):
        result = dfs((a, 0), goal, jug1_cap, jug2_cap, visited)
        if result is not None:
            return result
    # pour jug 1 into jug 2
    if a > 0 and b < jug2_cap:
        temp = min(a, jug2_cap - b)
        if not is_visited((a-temp, b+temp), visited):
            result = dfs((a-temp, b+temp), goal, jug1_cap, jug2_cap, visited)
            if result is not None:
                return result
    # pour jug 2 into jug 1
    if b > 0 and a < jug1_cap:
        temp = min(b, jug1_cap - a)
        if not is_visited((a+temp, b-temp), visited):
            result = dfs((a+temp, b-temp), goal, jug1_cap, jug2_cap, visited)
            if result is not None:
                return result
    return None

# Example usage
jug1_cap = 4
jug2_cap = 3
start = (0, 0)
goal = (2, 0)

visited = []
result = dfs(start, goal, jug1_cap, jug2_cap, visited)
if result is None:
    print("No solution found.")
else:
    print("Solution found: ", result)
