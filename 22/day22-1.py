lines = open("day22.txt","r").read().split("\n")
data = []
for i in lines:
    # x1, x2, y1, y2, z1, z2
    t,i = i.split()
    t = {"off":0,"on":1}[t]
    i = i.replace("x=","").replace("y=","").replace("z=","").replace("..",",").split(",")
    data.append([int(j)+50 for j in i]+[t])
map = [[[0]*101 for i in range(101)] for j in range(101)]
for i in data:
    for a in range(i[0], i[1]+1):
        if 0 <= a <= 100:
            for b in range(i[2], i[3]+1):
                if 0 <= b <= 100:
                    for c in range(i[4], i[5]+1):
                        if 0 <= c <= 100:
                            map[a][b][c] = i[6]
print(sum([sum([sum([k for k in i]) for i in j]) for j in map]))