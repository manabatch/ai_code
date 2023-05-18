REWARD = -0.01
DISCOUNT = 0.5
MAX_ERROR = 1e-3
NUM_ACTIONS = 4
ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
NUM_ROW = 3
NUM_COL = 4
U = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]

def getU(U, r, c, action):
    dr, dc = ACTIONS[action]
    newR, newC = r + dr, c + dc
    if newR < 0 or newC < 0 or newR >= NUM_ROW or newC >= NUM_COL or (newR == newC == 1):
        return U[r][c]
    else:
        return U[newR][newC]

def calculateU(U, r, c, action):
    u = REWARD
    u += 0.1 * DISCOUNT * getU(U, r, c, (action - 1) % 4)
    u += 0.8 * DISCOUNT * getU(U, r, c, action)
    u += 0.1 * DISCOUNT * getU(U, r, c, (action + 1) % 4)
    return u

def valueIteration(U):
    print("The initial state is:")
    for row in U:
        print(" | ".join(f"{val:5}" for val in row))
    print("\nDuring the value iteration:")
    iteration = 0
    while True:
        nextU = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]
        error = 0
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if (r <= 1 and c == 3) or (r == c == 1):
                    continue
                nextU[r][c] = max([calculateU(U, r, c, action) for action in range(NUM_ACTIONS)])
                error = max(error, abs(nextU[r][c] - U[r][c]))
        U = nextU
        for row in U:
            print(" | ".join(f"{val:5.2f}" for val in row))
        print()
        iteration += 1
        if error < MAX_ERROR or iteration > 10:  # Stop condition modified for faster execution
            break
    return U

U = valueIteration(U)
print("\nThe optimal policy is:")
for row in U:
    print(" | ".join(f"{val:5.2f}" for val in row))

