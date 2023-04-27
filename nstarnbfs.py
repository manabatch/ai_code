from collections import deque

def bfs(grid, start):
    # Define the colors available for coloring the cells
    colors = ['R', 'G','B','Y']

    # Define a dictionary to keep track of visited cells and their color
    visited = {}

    # Define a queue to store cells to visit
    queue = deque()
    queue.append(start)

    # Start BFS traversal
    while queue:
        cell = queue.popleft()
        row, col = cell[0], cell[1]

        # Check if cell has already been visited
        if cell in visited:
            continue

        # Assign a color to the current cell that is not the same as its neighbors
        for color in colors:
            if color not in [visited.get((row-1, col)), visited.get((row+1, col)), visited.get((row, col-1)), visited.get((row, col+1)), visited.get((row-1, col-1)), visited.get((row+1, col-1)), visited.get((row-1, col+1)), visited.get((row+1, col+1))]:
                visited[cell] = color
                break

        # Add unvisited neighbors to the queue
        if row > 0:
            queue.append((row-1, col))
        if col > 0:
            queue.append((row, col-1))
        if col < len(grid)-1:
            queue.append((row, col+1))
        if row < len(grid)-1:
            queue.append((row+1, col))
        if col > 0 and row > 0:
            queue.append((row-1, col-1))
        if col > 0 and row < len(grid)-1:
            queue.append((row+1, col-1))
        if col < len(grid)-1 and row > 0:
            queue.append((row-1, col+1))
        if col < len(grid)-1 and row < len(grid)-1:
            queue.append((row+1, col+1))

    return visited

# Example usage
grid = [['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', '']]

# Define the grid size
N = 4
visited = bfs(grid, (0, 0))

# Print the grid with the colored cells
for i in range(N):
    for j in range(N):
        if (i, j) in visited:
            print(visited[(i, j)], end=' ')
        else:
            print('_', end=' ')
    print()
