data = open("day13.txt").read().splitlines()
points = []
for c, i in enumerate(data):
    if len(i) == 0:
        break
    points.append(list(map(int,i.split(","))))
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
print(len(set(map(tuple,points))))