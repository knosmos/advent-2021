from copy import deepcopy
state = [list(i) for i in open("day25.txt","r").read().split("\n")]
rows = len(state)
cols = len(state[0])
nstate = [["."]*cols for _ in range(rows)]
c = 0
while True:
    nstate = [["."]*cols for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            if state[y][x] == ">":
                if state[y][(x+1)%cols] == ".":
                    nstate[y][(x+1)%cols] = ">"
                else:
                    nstate[y][x] = ">"
            if state[y][x] == "v": nstate[y][x] = "v"
    nstate1 = deepcopy(nstate)
    #print("\n".join(["".join(i) for i in nstate])+"\n")
    for y in range(rows):
        for x in range(cols):
            if state[y][x] == "v":
                if nstate1[(y+1)%rows][x] == ".":
                    nstate[(y+1)%rows][x] = "v"
                    nstate[y][x] = "."
                else:
                    nstate[y][x] = "v"
    c += 1
    if state == nstate:
        break
    state = nstate
    nstate = [["."]*cols for _ in range(rows)]
    #print("\n".join(["".join(i) for i in state])+"\n")
print(c)