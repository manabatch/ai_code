import random

REWARD = -0.01
DISCOUNT = 0.99
MAX_ERROR = 1e-3
NUM_ACTIONS = 4
ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
NUM_ROW = 3
NUM_COL = 4
U = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]
policy = [[random.choice(["Down", "Left", "Up", "Right"]) for _ in range(NUM_COL)] for _ in range(NUM_ROW)]

def getU(r, c, action, U):
    dr, dc = ACTIONS[action]
    newR, newC = r + dr, c + dc
    if newR < 0 or newC < 0 or newR >= NUM_ROW or newC >= NUM_COL or (newR == newC == 1):
        return U[r][c]
    else:
        return U[newR][newC]

def calculateU(r, c, action, U):
    u = REWARD
    u += 0.1 * DISCOUNT * getU(r, c, (action - 1) % 4, U)
    u += 0.8 * DISCOUNT * getU(r, c, action, U)
    u += 0.1 * DISCOUNT * getU(r, c, (action + 1) % 4, U)
    return u

def policyEvaluation(policy, U):
    while True:
        nextU = [[calculateU(r, c, policy[r][c], U) for c in range(NUM_COL)] for r in range(NUM_ROW)]
        if max(abs(nextU[r][c] - U[r][c]) for r in range(NUM_ROW) for c in range(NUM_COL) if (r <= 1 and c != 3) and not (r == c == 1)) < MAX_ERROR * (1 - DISCOUNT) / DISCOUNT:
            return nextU
        U = nextU

def policyIteration(policy):
    U = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]
    iteration = 0
    print("The initial random policy is:")
    printPolicy(policy)
    print("\nDuring the policy iteration:")
    while True:
        U = policyEvaluation(policy, U)
        unchanged = True
        iteration += 1
        print("\nIteration:", iteration)
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if (r <= 1 and c == 3) or (r == c == 1):
                    continue
                maxAction = max(range(NUM_ACTIONS), key=lambda action: calculateU(r, c, action, U))
                if maxAction != policy[r][c]:
                    policy[r][c] = maxAction
                    unchanged = False
        printPolicy(policy)
        if unchanged:
            return policy

def printPolicy(policy):
    action_symbols = ["Down", "Left", "Up", "Right"]
    for row in policy:
        print("|", end=" ")
        for action in row:
            print(action_symbols[action].ljust(5), end=" ")
        print("|")

# Convert policy from symbols to indices
for i in range(NUM_ROW):
    for j in range(NUM_COL):
        policy[i][j] = ["Down", "Left", "Up", "Right"].index(policy[i][j])

policy = policyIteration(policy)

print("\nThe optimal policy is:")
printPolicy(policy)
