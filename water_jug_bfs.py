from queue import Queue
def is_goal(state,goal):
    if(state[0]==goal[0] and state[1]==goal[1]):
        return True
    return False
def is_visited(state,visited):
    for i in visited:
        if(i==state):
            return True
    return False
def bfs(start,goal,j1,j2):
    q=Queue()
    visited=[]
    q.put(start)
    visited.append(start)
    while not q.empty():
        current=q.get()
        if(is_goal(current,goal)):
            return current,visited
        a,b=current
        if(a<j1 and not is_visited((j1,b),visited)):
            q.put((j1,b))
            visited.append((j1,b))
        if(b<j2 and not is_visited((a,j2),visited)):
            q.put((a,j2))
            visited.append((a,j2))
        if(a>0 and not is_visited((0,b),visited)):
            q.put((0,b))
            visited.append((0,b))
        if(b>0 and not is_visited((a,0),visited)):
            q.put((a,0))
            visited.append((a,0))
        if(a>0 and b<j2):
            temp=min(a,j2-b)
            if(not is_visited((a-temp,b+temp),visited)):
                q.put((a-temp,b+temp))
                visited.append((a-temp,b+temp))
        if(b>0 and a<j2):
            temp=min(j1-a,b)
            if(not is_visited((a+temp,b-temp),visited)):
                q.put((a+temp,b-temp))
                visited.append((a+temp,b-temp))
    return None

j1=4
j2=3
start=(0,0)
goal=(2,0)
print(bfs(start,goal,j1,j2))

        