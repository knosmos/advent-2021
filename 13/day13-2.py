data = open("day13.txt").read().splitlines()
points = []
for c, i in enumerate(data):
    if len(i) == 0:
        break
    points.append(list(map(int,i.split(","))))

m = [[0]*2000 for _ in range(2000)]
for i in points:
    m[i[0]][i[1]] = 1
for i in range(12):
    c += 1
    instruction = data[c][11:]
    dir = instruction[0]
    val = int(instruction[2:])
    if dir == "x":
        for i in range(0,len(m)):
            if i < val:
                m[i] = [min(1,m[i][j]+m[val-i+val][j]) for j in range(len(m[i]))]
        m = m[:val]
    elif dir == "y":
        for i in range(0,len(m)):
            l = m[i][:val]
            r = m[i][val:][::-1]
            r = [0]*(len(l)-len(r)) + r
            m[i] = [min(1,l[j]+r[j]) for j in range(len(l))]
for i in range(len(m[0])):
    for j in range(len(m)):
        if m[j][i] == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()