import copy

class PuzzleState:
    def __init__(self, numbers): # initialize the data
        self.cells = []
        self.blankLocation = 0, 0
        # [0,1,2,3,4,5,6,7,8]
        k = 0
        for i in range(3):
            row = []
            for j in range(3):
                row.append(numbers[k])
                if numbers[k] == 0:
                    self.blankLocation = i, j
                k += 1
            self.cells.append(row)

    def printState(self): # the current state
        lines = []
        horizontalline = ("_" * (13))
        print(horizontalline)
        for row in self.cells:
            rowline = "|"
            for col in row:
                if col == 0:
                    col = "."
                rowline = rowline + " " + col.__str__() + "|"
            print(rowline)
        print(horizontalline)

    def isGoal(self):
        current = [1,2,3,4,5,6,7,8,0]
        # current=[0,1,2,3,4,5,6,7,8]
        ele=0
        for i in range(3):
            for j in range(3):
                if current[ele] != self.cells[i][j]:
                    return False
                ele+=1
        return True

    def legalMoves(self):
        # return all the legal moves
        row, col = self.blankLocation
        legalMoves = []
        if row != 0:
            legalMoves.append("up")
        if row != 2:
            legalMoves.append("down")
        if col != 0:
            legalMoves.append("left")
        if col != 2:
            legalMoves.append("right")
        return legalMoves

    def resultState(self, move):
        # return the next state based on the move
        row, col = self.blankLocation
        if move == "up":
            newrow = row-1
            newcol = col
        elif move == "down":
            newrow = row+1
            newcol = col
        elif move == "left":
            newrow = row
            newcol = col - 1
        elif move == "right":
            newrow = row
            newcol = col+1
        else:
            raise "illegal move"
        newPuzzle = PuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])
        newPuzzle.cells = [value[:] for value in self.cells]
        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]
        newPuzzle.blankLocation = newrow, newcol
        return newPuzzle

    def eq(self, other):
        for row in range(3):
            if self.cells[row] != other.cells[row]:
                return False
        return True


class SearchProblem:
    def __init__(self, state):
        # initialize the search problem
        self.puzzle = state

    def getStartState(self):
        # return the start state
        return self.puzzle

    def getSuccessors(self, state):
        # return all the child states
        succs = []
        for move in state.legalMoves():
            cState = state.resultState(move)
            succs.append((cState, move))
        return succs
    def isGoalState(self, state):

# return information that state is goal state or not 
        return state.isGoal()
class Queue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


def BFS(problem):
    state = problem.getStartState()
    queue = Queue()
    action = ""
    fPath = []
    visitedStates = []
    queue.push(((state, action), fPath))
    counter = 0
    while queue.isEmpty() == False:
        current = queue.pop()
        cStatewithAction = current[0]
        cPath = current[1]

        cState = cStatewithAction[0]
        cAction = cStatewithAction[1]

        if cState in visitedStates:
            continue
        else:
            visitedStates.append(cState)

            counter += 1
            if problem.isGoalState(cState):
                # Goal found
                return cPath
            else:
                succs = problem.getSuccessors(cState)
                for succ in succs:
                    sPath = copy.deepcopy(cPath)
                    if succ[0] in visitedStates:
                        # already present
                        continue
                    else:
                        sPath.append(succ[1])
                        queue.push((succ, sPath))


puzzle = PuzzleState([1, 2, 3, 0, 4, 6, 7, 5, 8])
#goal_state=[1, 2, 3, 4, 5, 6, 7, 8, 0]
print("START STATE - ")
puzzle.printState()
p = SearchProblem(puzzle)
path = BFS(p)
print(path)
for p in path:
    puzzle = puzzle.resultState(p)
    puzzle.printState()
    input("Press Enter")
print("Goal state is reached")





