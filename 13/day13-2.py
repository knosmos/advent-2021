data = open("day13.txt").read().splitlines()
points = []
for c, i in enumerate(data):
    if len(i) == 0:
        break
    points.append(list(map(int,i.split(","))))
for i in range(12):
    c += 1
    k = data[c][11:]
    dir = k[0]
    val = int(k[2:])
    if dir == "x":
        for i in points:
            if i[0] > val: i[0] = val-(i[0]-val)
    elif dir == "y":
        for i in points:
            if i[1] > val: i[1] = val-(i[1]-val)
m = [[0]*6 for _ in range(40)]
for i in points:
    m[i[0]][i[1]] = 1
for i in range(6):
    for j in range(40):
        if m[j][i] == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()