data = open("day13.txt").read().splitlines()
points = []
for c, i in enumerate(data):
    if len(i) == 0:
        break
    points.append(list(map(int,i.split(","))))
instruction = data[c+1][11:]
dir = instruction[0]
val = int(instruction[2:])

m = [[0]*2000 for _ in range(2000)]
for i in points:
    m[i[0]][i[1]] = 1
if dir == "x":
    for i in range(0,2000):
        if i < val:
            m[i] = [min(1,m[i][j]+m[val-i+val][j]) for j in range(2000)]
    m = m[:val]
print(sum(sum(i) for i in m))