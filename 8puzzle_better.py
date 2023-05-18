from heapq import heappush , heappop

def solve_8puzzle(initialstate):
    goalstate = '12345678_'
    moves = {'U':-3,'D':3,'L':-1,'R':1}
    calculatecost = lambda state : sum(abs(i%3 - state.index(str((i+1)%9))%3) + abs(i//3 - state.index(str((i+1)%9))//3) for i in range(8))
    openlist=[]
    closedset=set()
    heappush(openlist,(calculatecost(initialstate),0,initialstate))
    while openlist:
        _,_,currentstate = heappop(openlist)
        closedset.add(currentstate)
        print_state(currentstate)
        if(currentstate == goalstate):
            return 
        zero_index = currentstate.index("_")
        for move, step in moves.items():
            new_index = zero_index + step
            if 0 <= new_index < 9 and (move != "L" or zero_index % 3 != 0) and (move != "R" or zero_index % 3 != 2):
                new_state = list(currentstate)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                new_state = "".join(new_state)

                if new_state not in closedset:
                    heappush(openlist, (calculatecost(new_state), 0, new_state))
    print("no solution found")
    
    
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

initialstate = "123_46758"
solve_8puzzle(initialstate)
