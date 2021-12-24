from collections import deque
from copy import deepcopy as dc

rooms = [
    ["D","B"],
    ["A","A"],
    ["B","D"],
    ["C","C"]
]
rooms = [
    ["A","A"],
    ["C","B"],
    ["B","C"],
    ["D","D"]
]
correct = "ABCD"
hall = ["."]*11
doors = [2,4,6,8]
costs = {"A":1,"B":10,"C":100,"D":1000}

mem = {}

def pr(state):
    r,hall,_ = state
    r = dc(r)
    for i in range(4):
        while len(r[i])<2: r[i].append(".")
    print("".join(hall))
    print(f"  {r[0][0]}|{r[1][0]}|{r[2][0]}|{r[3][0]}")
    print(f"  {r[0][1]}|{r[1][1]}|{r[2][1]}|{r[3][1]}")
    print()

def run(state):
    # State: [rooms, hall, cost]
    # Possible moves:
    # 1) move a pod out
    new_states = []
    rooms, hall, cost = state
    for i in range(4):
        if not rooms[i]: continue
        c = costs[rooms[i][0]] * (3-len(rooms[i]))
        nl = []
        for p in range((i+1)*2+1, 11):
            if hall[p] == ".": nl.append(p)
            else: break
        for p in range((i+1)*2-1, -1, -1):
            if hall[p] == ".": nl.append(p)
            else: break
        for np in nl:
            if not np in [2,4,6,8]:
                new_rooms = [r[:] for r in rooms]
                new_rooms[i].pop(0)
                
                new_hall = hall[:]
                new_hall[np] = rooms[i][0]

                new_states.append([
                    new_rooms,
                    new_hall,
                    cost + c + abs(np-(i+1)*2) * costs[rooms[i][0]]
                ])

    # 2) move a pod in the hall into a room
    for i in range(11):
        if hall[i] == ".":
            continue
        nl = []
        for p in range(i+1, 11):
            if hall[p] == ".": nl.append(p)
            else: break
        for p in range(i-1, -1, -1):
            if hall[p] == ".": nl.append(p)
            else: break
        for np in nl:
            if np in [2,4,6,8]:
                if hall[i] != "ABCD"[np//2-1]: continue
                c = costs[hall[i]] * (3-len(rooms[np//2-1]))
                for j in rooms[np//2-1]:
                    if j != hall[i] or j != "ABCD"[np//2-1]:
                        break
                else:
                    new_rooms = [r[:] for r in rooms]
                    new_rooms[np//2-1].append(hall[i])
                    
                    new_hall = hall[:]
                    new_hall[i] = '.'

                    new_states.append([
                        new_rooms,
                        new_hall,
                        cost + c + abs(np-i) * costs[hall[i]]
                    ])
    return new_states

visited = set()
queue = deque([[rooms, hall, 0]])
while queue:
    x = queue.popleft()
    s = (tuple(map(tuple,x[0])), tuple(x[1]))
    if s in visited:
        continue
    #pr(x)
    visited.add(s)
    res = run(x)
    for i in res:
        if (tuple(map(tuple,i[0])), tuple(i[1])) in visited:
            continue
        queue.append(i)
        if i[0] == [[a]*2 for a in "ABCD"]:
            print(i)